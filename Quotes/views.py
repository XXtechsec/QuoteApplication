from django.shortcuts import render, redirect
from Quotes.forms import QuoteForm
from django.http import HttpResponse
from django.template import loader
from Quotes.models import *
from django.forms.models import model_to_dict
from django.template import Context
from django.shortcuts import render_to_response
import ast
from .models import *
from .render import Render
from django.views.generic import View
import operator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

z = []
total = 0
LookUp = {}
selectedQuoteName = 'untitled'
selectedQuoteCompany = 'untitled'
def home(request):
    z = []
    return render(request, 'Quotes/home.html')



def result(request):
    if 'add' in request.POST:
        global z
        p = ast.literal_eval(request.POST['add'])
        z.append(p.copy())
        messages.success(request, "Successfully Added "+ p['Description'])
    return QuoteMaker(request)

def delete(request):
    if 'deleteService' in request.POST:
        global total
        todelete = ast.literal_eval(request.POST['deletebtn'])
        messages.success(request, "Successfully Deleted "+ todelete['Description'])
        z.remove(todelete)
        return QuoteMaker(request)
    if 'deleteQuote' in request.POST:
        Quote.objects.filter(Name=selectedQuoteName).delete()
        return select(request)
        messages.success(request, "Successfully Deleted: "+ selectedQuoteName)

        messages.success(request, "Didn't work!")
    if 'clear' in request.POST:
        z.clear()
        return QuoteMaker(request)



def changeQuality(request):
    global z
    global LookUp
    try:
        ToChangeQuality = ast.literal_eval(request.POST['ToChangeQuality'])
        Sku = ToChangeQuality['SKU']
        Quality = request.POST['dropdown']
        if (ToChangeQuality['SKU'].endswith('.G') or ToChangeQuality['SKU'].endswith('.S')):
            Sku = ToChangeQuality['SKU'][:-2]
        if(Quality == 'Bronze'):
            Sku = Sku + ''
        if(Quality == 'Silver'):
            Sku = Sku + '.S'
        if(Quality == 'Gold'):
            Sku = Sku + '.G'
        TheChange = Service.objects.filter(SKU = Sku).values()[0]
        TheChange['Qty'] = ToChangeQuality['Qty']
        indexToChange = z.index(ToChangeQuality)
        z[indexToChange] = TheChange
        messages.success(request, "Successfully Changed the Quality of " + ToChangeQuality['Description'] + " to " + Quality)
    except:
        messages.error(request, "Could not change quality!")
    return QuoteMaker(request)

@login_required
def QuoteMaker(request):
    global total
    global z
    global selectedQuoteName
    global selectedQuoteCompany
    total = 0
    for o in z:
        total += (o['Price']*float(o['Qty']))


    for q in Service.objects.values_list('Type', flat=True).distinct():
        LookUp.update({q: list(Service.objects.filter(Type=q).values_list('Quality', flat=True).distinct())})

    context = {
        'Service': Service.objects.values('Price', 'Description', 'ServiceType', 'Type', 'Quality', 'SKU', 'Qty'),
        'LookUp': sorted(LookUp.items()),
        'type': sorted(Service.objects.values_list('Type', flat=True).distinct()),
        'quality': sorted(Service.objects.values_list('Quality', flat=True).distinct()),
        'result': z,
        'total': total,
        'name': selectedQuoteName,
        'company': selectedQuoteCompany
    }

    return render(request, 'Quotes/QuoteMaker.html', context)

def Pdf(request):
    params = {
        'products': z,
        'total': total,
    }
    return Render.render('Quotes/pdf.html', params)

def CSV(request):
    global z
    global selectedQuoteName
    model_class = Service

    meta = model_class._meta
    field_names = ['ServiceType', 'Type', 'Quality', 'SKU', 'Description', 'Price', 'Qty']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + selectedQuoteName + '.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in z:
        row = writer.writerow(obj[field] for field in field_names)

    return response

def saveQuote(request):
    global z
    saveName = request.POST['saveName']
    saveCompany = request.POST['saveCompany']
    if z != []:
        if Quote.objects.filter(Name=saveName).exists() == False:
            obj = Quote.objects.create(Name=saveName, Company=saveCompany)
            for i in z:
                obj.Services.add(Service.objects.get(SKU=i['SKU']))

            obj.save()
            messages.success(request, "Successfully Created " + saveName)
            z = []
            return select(request)
        else:
            obj = Quote.objects.get(Name=saveName)
            obj.Services.set('')
            for i in z:
                obj.Services.add(Service.objects.get(SKU=i['SKU']))
            messages.success(request, "Successfully Updated " + saveName)
            z.clear()
            return select(request)

def Qty(request):
    try:
        global z
        toChangeQty = ast.literal_eval(request.POST['ToChange'])
        qty = request.POST['Qty']
        if(qty != ''):
            indexToChange = z.index(toChangeQty)
            toChangeQty['Qty'] = qty
            z[indexToChange] = toChangeQty
            messages.success(request, "Successfully Changed the Qty of " + toChangeQty['Description'] + " to " + qty)
    except:
        messages.error(request, "Went too fast!")
    return QuoteMaker(request)

def search(request):
    global z
    global total
    search = request.POST['userSearch']
    searchResults = Service.objects.filter(Description__icontains=search).exclude(Description__contains="Silver").exclude(Description__contains="Gold")

    contextS = {
        'Service': searchResults.values('Price', 'Description', 'ServiceType', 'Type', 'Quality', 'SKU', 'Qty'),
        'result': z,
        'total': total,
        'search': search,
    }
    userSearch = request.POST['userSearch']
    return render(request, 'Quotes/Search.html', contextS)

@login_required
def select(request):
    global z
    global selectedQuoteName
    global selectedQuoteCompany
    if 'new' in request.POST:
        z.clear()
        selectedQuoteCompany = 'untitled'
        selectedQuoteName = 'untitled'
        return QuoteMaker(request)
    elif 'old' in request.POST:
        z.clear()
        selectedQuote = ast.literal_eval(request.POST['old'])
        selectedQuoteName = request.POST['oldName']
        selectedQuoteCompany = list(Quote.objects.filter(Name=selectedQuoteName).values_list('Company', flat=True))
        selectedQuoteCompany = ''.join(selectedQuoteCompany)
        for id in selectedQuote:
            z.append(Service.objects.filter(pk=id).values()[0])
        return QuoteMaker(request)

    else:
        LookUpQuote = {}
        for Name in Quote.objects.values_list('Name', flat=True):
            LookUpQuote.update({Name: list(Quote.objects.filter(Name=Name).values_list('Services', flat=True))})
        contextSelect= {
            'LookUpQuote': LookUpQuote.items(),
        }
        return render(request, 'Quotes/select.html', contextSelect)
