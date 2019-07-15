import csv
from Quotes.models import Service
from django.http import HttpResponse
with open('Quotes/services_db.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Service(ServiceTypeService=row['ServiceTypeService'], TypeService=row['TypeService'],QualityService=row['QualityService'], SKUService=row['SKUService'], DescriptionService=row['DescriptionService'],priceService=row['priceService'], QtyService = 1)
        if(Service.objects.filter(SKUService = p.SKUService).exists()):
            print('that exists!')
        else:
            p.save()
            print(p)
