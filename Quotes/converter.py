import csv
from Quotes.models import Service
from django.http import HttpResponse
with open('Quotes/services_db.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Service(ServiceType=row['ServiceType'], Type=row['Type'],Quality=row['Quality'], SKU=row['SKU'], Description=row['Description'],price=row['price'], Qty = 1)
        if(Service.objects.filter(SKU = p.SKU).exists()):
            print('that exists!')
        else:
            p.save()
            print(p)
