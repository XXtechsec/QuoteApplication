from django.shortcuts import render, redirect
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
from django.contrib.auth.models import User
import csv
from datetime import datetime

total = 0
LookUp = {}
UserLookUp = {}
selectedQuoteName = 'untitled'
selectedQuoteCompany = 'untitled'
selectedQuoteContact = 'untitled'
def home(request):
    z = []
    request.session['listOfProducts'] = []
    return render(request, 'Quotes/home.html')

def result(request):
    if 'add' in request.POST:
        global UserLookUp
        z = UserLookUp.get(request.user.id, [])
        p = ast.literal_eval(request.POST['add'])
        z.append(p.copy())
        UserLookUp[request.user.id] = z
        messages.success(request, "Successfully Added "+ p['DescriptionService'])
    return QuoteMaker(request)

def delete(request):
    if 'deleteService' in request.POST:
        global total
        global UserLookUp
        z = UserLookUp.get(request.user.id, [])
        todelete = ast.literal_eval(request.POST['deleteService'])
        messages.success(request, "Successfully Deleted "+ todelete['DescriptionService'])
        z.remove(todelete)
        UserLookUp[request.user.id] = z
        return QuoteMaker(request)
    if 'deleteQuote' in request.POST:
        Quote.objects.filter(Name=selectedQuoteName).delete()
        return select(request)
        messages.success(request, "Successfully Deleted: "+ selectedQuoteName)

        messages.success(request, "Didn't work!")
    if 'clear' in request.POST:
        z = UserLookUp.get(request.user.id, [])
        z.clear()
        UserLookUp[request.user.id] = z
        return QuoteMaker(request)

def changeQuality(request):
    global UserLookUp
    global LookUp
    z = UserLookUp.get(request.user.id, [])
    try:
        ToChangeQuality = ast.literal_eval(request.POST['ToChangeQuality'])
        Sku = ToChangeQuality['SKUService']
        QualityService = request.POST['dropdown']
        if (ToChangeQuality['SKUService'].endswith('.G') or ToChangeQuality['SKUService'].endswith('.S')):
            Sku = ToChangeQuality['SKUService'][:-2]
        if(QualityService == 'Bronze'):
            Sku = Sku + ''
        if(QualityService == 'Silver'):
            Sku = Sku + '.S'
        if(QualityService == 'Gold'):
            Sku = Sku + '.G'
        TheChange = Service.objects.filter(SKUService = Sku).values()[0]
        TheChange['QtyService'] = ToChangeQuality['QtyService']
        indexToChange = z.index(ToChangeQuality)
        z[indexToChange] = TheChange
        messages.success(request, "Successfully Changed the QualityService of " + ToChangeQuality['DescriptionService'] + " to " + QualityService)
    except:
        messages.error(request, "Could not change quality!")
    UserLookUp[request.user.id] = z
    return QuoteMaker(request)

@login_required
def QuoteMaker(request):
    global total
    global UserLookUp
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact
    z = UserLookUp.get(request.user.id, [])
    total = 0
    for o in z:
        total += (o['priceService']*float(o['QtyService']))

    for q in Service.objects.values_list('TypeService', flat=True).distinct():
        LookUp.update({q: list(Service.objects.filter(TypeService=q).values_list('QualityService', flat=True).distinct())})

    context = {
        'Service': Service.objects.values('priceService', 'DescriptionService', 'ServiceTypeService', 'TypeService', 'QualityService', 'SKUService', 'QtyService'),
        'LookUp': sorted(LookUp.items()),
        'type': sorted(Service.objects.values_list('TypeService', flat=True).distinct()),
        'quality': sorted(Service.objects.values_list('QualityService', flat=True).distinct()),
        'result': z,
        'total': total,
        'name': selectedQuoteName,
        'company': selectedQuoteCompany,
        'contact': selectedQuoteContact
    }
    return render(request, 'Quotes/QuoteMaker.html', context)

def Pdf(request):
    global selectedQuoteContact
    global selectedQuoteCompany
    global UserLookUp
    z = UserLookUp.get(request.user.id, [])
    params = {
        'products': z,
        'total': total,
        'User': request.user,
        'company': selectedQuoteCompany,
        'contact': selectedQuoteContact,
        'Date': datetime.now().strftime("%Y-%m-%d")
    }

    return Render.render('Quotes/pdf.html', params)

def CSV(request):
    global UserLookUp
    global selectedQuoteName
    z = UserLookUp.get(request.user.id, [])
    model_class = Service

    meta = model_class._meta
    field_names = ['ServiceTypeService', 'TypeService', 'QualityService', 'SKUService', 'DescriptionService', 'priceService', 'QtyService']

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + selectedQuoteName + '.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in z:
        row = writer.writerow(obj[field] for field in field_names)

    return response

def saveQuote(request):
    global UserLookUp
    saveName = request.POST['saveName']
    saveCompany = request.POST['saveCompany']
    saveContact = request.POST['saveContact']
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact
    z = UserLookUp.get(request.user.id, [])
    if z != []:
        if Quote.objects.filter(Name=saveName).exists() == False:
            obj = Quote.objects.create(Name=saveName, Company=saveCompany, Contact=saveContact)
            for i in z:
                obj.Services.add(Service.objects.get(SKUService=i['SKUService']))

            obj.save()
            messages.success(request, "Successfully Created " + saveName)
            selectedQuoteName = saveName
            selectedQuoteCompany = saveCompany
            selectedQuoteContact = saveContact
            return QuoteMaker(request)
        else:
            obj = Quote.objects.get(Name=saveName)
            obj.Services.set('')
            for i in z:
                obj.Services.add(Service.objects.get(SKUService=i['SKUService']))
            Quote.objects.update(Company=saveCompany, Contact=saveContact)
            messages.success(request, "Successfully Updated " + saveName)
            selectedQuoteCompany = saveCompany
            selectedQuoteContact = saveContact
            return QuoteMaker(request)

def Qty(request):
    try:
        global UserLookUp
        z = UserLookUp.get(request.user.id, [])
        toChangeQty = ast.literal_eval(request.POST['ToChange'])
        qty = request.POST['QtyService']
        if(qty != ''):
            indexToChange = z.index(toChangeQty)
            toChangeQty['QtyService'] = qty
            z[indexToChange] = toChangeQty
            messages.success(request, "Successfully Changed the QtyService of " + toChangeQty['DescriptionService'] + " to " + qty)
    except:
        messages.error(request, "Went too fast!")
    UserLookUp[request.user.id] = z
    return QuoteMaker(request)

def search(request):
    global UserLookUp
    global total
    z = UserLookUp.get(request.user.id, [])
    search = request.POST['userSearch']
    searchResults = Service.objects.filter(Description__icontains=search).exclude(Description__contains="Silver").exclude(Description__contains="Gold")

    contextS = {
        'Service': searchResults.values('priceService', 'DescriptionService', 'ServiceTypeService', 'TypeService', 'QualityService', 'SKUService', 'QtyService'),
        'result': z,
        'total': total,
        'search': search,
    }
    userSearch = request.POST['userSearch']
    return render(request, 'Quotes/Search.html', contextS)

@login_required
def select(request):
    global UserLookUp
    global selectedQuoteName
    global selectedQuoteCompany
    global selectedQuoteContact
    z = UserLookUp.get(request.user.id, [])
    if 'new' in request.POST:
        z.clear()
        UserLookUp[request.user.id] = z
        return QuoteMaker(request)
    elif 'old' in request.POST:
        z.clear()
        selectedQuote = ast.literal_eval(request.POST['old'])
        selectedQuoteName = request.POST['oldName']
        selectedQuoteCompany = list(Quote.objects.filter(Name=selectedQuoteName).values_list('Company', flat=True))
        selectedQuoteCompany = ''.join(selectedQuoteCompany)
        selectedQuoteContact = list(Quote.objects.filter(Name=selectedQuoteName).values_list('Contact', flat=True))
        selectedQuoteContact = ''.join(selectedQuoteContact)
        for id in selectedQuote:
            z.append(Service.objects.filter(pk=id).values()[0])
        UserLookUp[request.user.id] = z
        return QuoteMaker(request)

    else:
        LookUpQuote = {}
        for Name in Quote.objects.values_list('Name', flat=True):
            LookUpQuote.update({Name: list(Quote.objects.filter(Name=Name).values_list('Services', flat=True))})
        contextSelect= {
            'LookUpQuote': LookUpQuote.items(),
        }
        return render(request, 'Quotes/select.html', contextSelect)
