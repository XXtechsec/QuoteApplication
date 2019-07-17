#where the magic happens
from django.shortcuts import render
from django.http import HttpResponse
from Quotes.models import *
from django.template import Context
from .render import Render
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import csv
import ast
from datetime import datetime

#!note through out the program I use selectedProducts, this is just a temporary variable in order to edit the product list trapped in UserLookUp[request.user.id] it is cleared at the end of every function

# Define variables for global usage
total = 0

#for mapping type with subtype !note I don't use the serviceType currently
LookUp = {}

#for mapping each product list to a user so multiple users can work at once
UserLookUp = {}

#Default values
selectedQuoteName = 'untitled'
selectedQuoteCompany = 'untitled'
selectedQuoteContact = 'untitled'

#add whatever you want here just resets values currently
def home(request):

    return render(request, 'Quotes/home.html')

#add product
def result(request):
    #if a post request with add run the function
    if 'add' in request.POST:
        global UserLookUp

        selectedProducts = UserLookUp.get(request.user.id, [])
        #map the set given to it as a dictonary think of ast.literal_eval like set_to_dict
        p = ast.literal_eval(request.POST['add'])
        selectedProducts.append(p.copy())
        #set the product list of the user to selectedProducts
        UserLookUp[request.user.id] = selectedProducts
        messages.success(request, "Successfully Added "+ p['description'])
    #runs the Quotemaker function inorder to render the page
    return QuoteMaker(request)

#delete product
def delete(request):
    if 'deleteService' in request.POST:
        global total
        global UserLookUp
        #set the selectedProduct equal to the set of products of the user with that id or []
        selectedProducts = UserLookUp.get(request.user.id, [])
        #map the set given to it as a dictonary think of ast.literal_eval like set_to_dict
        todelete = ast.literal_eval(request.POST['deleteService'])
        messages.success(request, "Successfully Deleted "+ todelete['description'])
        selectedProducts.remove(todelete)
        UserLookUp[request.user.id] = selectedProducts
        #runs the Quotemaker function inorder to render the page
        return QuoteMaker(request)
    if 'deleteQuote' in request.POST:
        Quote.objects.filter(Name=selectedQuoteName).delete()
        messages.success(request, "Successfully Deleted: "+ selectedQuoteName)
        #runs the select instead of Quotemaker because the quote the user was working on was delete so they need to get a new one
        return select(request)


    if 'clear' in request.POST:
        selectedProducts = UserLookUp.get(request.user.id, [])
        selectedProducts.clear()
        UserLookUp[request.user.id] = selectedProducts
        #runs the Quotemaker function inorder to render the page
        return QuoteMaker(request)

#using SKU and what it ends with change the quality
def changeQuality(request):
    global UserLookUp
    global LookUp
    selectedProducts = UserLookUp.get(request.user.id, [])
    try:
        #map the set given to it as a dictonary think of ast.literal_eval like set_to_dict
        ToChangeQuality = ast.literal_eval(request.POST['ToChangeQuality'])
        Sku = ToChangeQuality['vendorpartnumber']
        category = request.POST['dropdown']
        #removes the letter
        if (ToChangeQuality['vendorpartnumber'].endswith('.G') or ToChangeQuality['vendorpartnumber'].endswith('.S')):
            Sku = ToChangeQuality['vendorpartnumber'][:-2]
        #uses what the user inputed to change it
        if(category == 'Bronze'):
            Sku = Sku + ''
        if(category == 'Silver'):
            Sku = Sku + '.S'
        if(category == 'Gold'):
            Sku = Sku + '.G'
        #get the product with the updated SKU
        TheChange = ProductsCommerxcatalogProducts.objects.filter(vendorpartnumber = Sku).values()[0]
        #update everything including deleting it from selectedProduct which in turn deletes it from UserLookUp
        TheChange['QtyService'] = ToChangeQuality['QtyService']
        indexToChange = selectedProducts.index(ToChangeQuality)
        selectedProducts[indexToChange] = TheChange
        messages.success(request, "Successfully Changed the category of " + ToChangeQuality['description'] + " to " + category)
    except:
        messages.error(request, "Could not change quality!")
    UserLookUp[request.user.id] = selectedProducts
    #renders the page using the QuoteMaker function
    return QuoteMaker(request)

#renders PDF
def Pdf(request):
    #!note Quote needs to be saved first
    global selectedQuoteContact
    global selectedQuoteCompany
    global UserLookUp
    selectedProducts = UserLookUp.get(request.user.id, [])
    #sets up the following context
    params = {
        'products': selectedProducts,
        'total': total,
        'User': request.user,
        'company': selectedQuoteCompany,
        'contact': selectedQuoteContact,
        #formats the data
        'Date': datetime.now().strftime("%Y-%m-%d")
    }
    #render the pdf using function in render.py using the context provided
    return Render.render('Quotes/pdf.html', params)

#renders CSV using the csv library
def CSV(request):
    global UserLookUp
    global selectedQuoteName

    selectedProducts = UserLookUp.get(request.user.id, [])
    model_class = ProductsCommerxcatalogProducts

    meta = model_class._meta
    field_names = ['vendorpartnumber', 'category', 'vendorpartnumber', 'description', 'list', 'QtyService']

    response = HttpResponse(content_type='text/csv')
    #sets up file name to QuoteName
    response['Content-Disposition'] = 'attachment; filename=' + selectedQuoteName + '.csv'.format(meta)
    writer = csv.writer(response)

    #for the fields specified in field_name write all objects selected
    writer.writerow(field_names)
    for obj in selectedProducts:
        row = writer.writerow(obj[field] for field in field_names)

    return response

#saves the quote for later use
def saveQuote(request):
    global UserLookUp
    #gets the info of the Quote
    saveName = request.POST['saveName']
    saveCompany = request.POST['saveCompany']
    saveContact = request.POST['saveContact']
    #gets variables to update
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact

    #get selected products
    selectedProducts = UserLookUp.get(request.user.id, [])
    #checks to make sure there is something to save
    if selectedProducts != []:
        #check to make sure the name given doesn't already exist
        if Quote.objects.filter(Name=saveName).exists() == False:
            #creates a new object with the values provided and adds all the services
            obj = Quote.objects.create(Name=saveName, Company=saveCompany, Contact=saveContact)
            for i in selectedProducts:
                obj.Services.add(ProductsCommerxcatalogProducts.objects.get(vendorpartnumber=i['vendorpartnumber']))

            #saves the object
            obj.save()

            messages.success(request, "Successfully Created " + saveName)
            selectedQuoteName = saveName
            selectedQuoteCompany = saveCompany
            selectedQuoteContact = saveContact
            #renders the page using the QuoteMaker function
            return QuoteMaker(request)

        #if name is taken update the Quote with that name
        else:
            #get the quote with that name
            obj = Quote.objects.get(Name=saveName)
            #resets the products stored and sets them to what the user currently has selected
            obj.Services.set('')
            for i in selectedProducts:
                obj.Services.add(ProductsCommerxcatalogProducts.objects.get(vendorpartnumber=i['vendorpartnumber']))
            #update any changes to the company or contact
            Quote.objects.update(Company=saveCompany, Contact=saveContact)
            messages.success(request, "Successfully Updated " + saveName)
            selectedQuoteCompany = saveCompany
            selectedQuoteContact = saveContact

            #renders the page using the QuoteMaker function
            return QuoteMaker(request)

#changes the Quantity of a specific product
def Qty(request):
    try:
        global UserLookUp
        #get all the products selected
        selectedProducts = UserLookUp.get(request.user.id, [])
        #map the set given to it as a dictonary think of ast.literal_eval like set_to_dict
        toChangeQty = ast.literal_eval(request.POST['ToChange'])
        #get the qty the user selected
        qty = request.POST['QtyService']
        #if its not nothing
        if(qty != ''):
            #simply change the Qty
            indexToChange = selectedProducts.index(toChangeQty)
            toChangeQty['QtyService'] = qty
            selectedProducts[indexToChange] = toChangeQty
            messages.success(request, "Successfully Changed the QtyService of " + toChangeQty['description'] + " to " + qty)
    except:
        messages.error(request, "Went too fast!")
    UserLookUp[request.user.id] = selectedProducts
    #renders the page using the QuoteMaker function
    return QuoteMaker(request)

#handles searches
def search(request):
    global UserLookUp
    global total
    selectedProducts = UserLookUp.get(request.user.id, [])
    #check if user want a search of product or quote
    if 'userSearch' in request.POST:
        #gets the search and gets all Service obj with that description minus silver and gold
        search = request.POST['userSearch']
        searchResults = ProductsCommerxcatalogProducts.objects.filter(Description__icontains=search).exclude(Description__contains="Silver").exclude(Description__contains="Gold")

        contextS = {
            'Service': searchResults.values('list', 'description', 'ServiceTypeService', 'vendorpartnumber', 'category', 'vendorpartnumber', 'QtyService'),
            'result': selectedProducts,
            'total': total,
            'search': search,
        }
        #renders the search.html with the given context
        return render(request, 'Quotes/Search.html', contextS)
    if 'quoteSearch' in request.POST:
        search = request.POST['quoteSearch']
        LookUpQuote = {}
        #set the Quotes to those that have the same name as the search
        for Name in Quote.objects.filter(Name__icontains=search).values_list('Name', flat=True):
            LookUpQuote.update({Name: list(Quote.objects.filter(Name=Name).values_list('Services', flat=True))})

        #gets all quotes if no search
        if search == None:
            for Name in Quote.objects.values_list('Name', flat=True):
                LookUpQuote.update({Name: list(Quote.objects.filter(Name=Name).values_list('Services', flat=True))})

        contextS= {
            'LookUpQuote': LookUpQuote.items(),
        }
        #render select.html with the given context
        return render(request, 'Quotes/select.html', contextS)

@login_required
def select(request):
    global UserLookUp
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact
    selectedProducts = UserLookUp.get(request.user.id, [])
    #if the user selects new
    if 'new' in request.POST:
        #easy, give the user an no selected Products or Quote info
        selectedProducts.clear()
        UserLookUp[request.user.id] = selectedProducts
        #renders the page using the QuoteMaker function
        return QuoteMaker(request)
    elif 'old' in request.POST:
        #hard, get the Quote the user requested and set all the info using it
        selectedProducts.clear()
        #map the set given to it as a dictonary think of ast.literal_eval like set_to_dict
        selectedQuote = ast.literal_eval(request.POST['old'])
        selectedQuoteName = request.POST['oldName']
        selectedQuoteCompany = list(Quote.objects.filter(Name=selectedQuoteName).values_list('Company', flat=True))
        selectedQuoteCompany = ''.join(selectedQuoteCompany)
        selectedQuoteContact = list(Quote.objects.filter(Name=selectedQuoteName).values_list('Contact', flat=True))
        selectedQuoteContact = ''.join(selectedQuoteContact)
        for id in selectedQuote:
            selectedProducts.append(ProductsCommerxcatalogProducts.objects.filter(pk=id).values()[0])
        UserLookUp[request.user.id] = selectedProducts
        #renders the page using the QuoteMaker function
        return QuoteMaker(request)

    else:
        #if no select display all Quotes
        LookUpQuote = {}
        for Name in Quote.objects.values_list('Name', flat=True):
            LookUpQuote.update({Name: list(Quote.objects.filter(Name=Name).values_list('Services', flat=True))})
        contextSelect= {
            'LookUpQuote': LookUpQuote.items(),
        }
        return render(request, 'Quotes/select.html', contextSelect)

@login_required
#Main function when loading the Quote Maker page
def QuoteMaker(request):
    #gets alot of variables
    global total
    global UserLookUp
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact
    selectedProducts = UserLookUp.get(request.user.id, [])
    total = 0
    #use temporary variable o inorder to get the total price
    for o in selectedProducts:
        total += (o['list']*float(o['QtyService']))
    #use temporary variable q to map the type to the give subtypes
    for q in ProductsCommerxcatalogProducts.objects.values_list('vendorpartnumber', flat=True).distinct():
        LookUp.update({q: list(ProductsCommerxcatalogProducts.objects.filter(vendorpartnumber=q).values_list('category', flat=True).distinct())})

    #use all the info given to it to make a context
    context = {
        'Service': ProductsCommerxcatalogProducts.objects.values('list', 'description', 'ServiceTypeService', 'vendorpartnumber', 'category', 'vendorpartnumber', 'QtyService'),
        'LookUp': sorted(LookUp.items()),
        'type': sorted(ProductsCommerxcatalogProducts.objects.values_list('vendorpartnumber', flat=True).distinct()),
        'quality': sorted(ProductsCommerxcatalogProducts.objects.values_list('category', flat=True).distinct()),
        'result': selectedProducts,
        'total': total,
        'name': selectedQuoteName,
        'company': selectedQuoteCompany,
        'contact': selectedQuoteContact
    }
    #renders the page using the context
    return render(request, 'Quotes/QuoteMaker.html', context)
