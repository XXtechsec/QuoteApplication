from django.db import models

class Service(models.Model):
    ServiceTypeService = models.CharField(max_length = 100)
    TypeService= models.CharField(max_length = 100)
    QualityService = models.CharField(max_length = 100)
    SKUService = models.CharField(max_length = 20)
    DescriptionService = models.CharField(max_length = 200)
    priceService = models.FloatField()
    QtyService = models.IntegerField(default=1)

    class Meta:
        managed = False
    def __str__(self):
        return self.DescriptionService

class Quote(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(Service)


    def __str__(self):
        return self.Name


class ProductsCommerxcatalogFolders(models.Model):
    foldername = models.CharField(db_column='FolderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    indentlevel = models.SmallIntegerField(db_column='IndentLevel', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Folders'

class ProductsCommerxcatalogProducts(models.Model):
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    folderlist = models.TextField(db_column='FolderList', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    list = models.FloatField(db_column='List', blank=True, null=True)  # Field name made lowercase.
    vendorpartnumber = models.CharField(db_column='VendorPartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Products'

def merge_models(apps, schema_editor):
    for obj in ProductsCommerxcatalogProducts.objects.all():
        if(obj.folderlist is None):
            thirdFolder = 'Other'
            secondFolder = '-'
            firstFolder = '-'
        else:
            firstFolder = ProductsCommerxcatalogFolders.objects.filter(id = obj.folderlist.replace('(', '').replace(')', '').replace('(83)', '').replace('(84)', '')).values()[0]
            print(firstFolder)
            secondFolder = ProductsCommerxcatalogFolders.objects.filter(id = firstFolder['parentid']).values()[0]
            print(secondFolder)
            thirdFolder = ProductsCommerxcatalogFolders.objects.filter(id = secondFolder['parentid']).values()[0]
            print(thirdFolder)
        service, created = Service.objects.get_or_create(
            ServiceTypeService = thirdFolder['foldername'],
            TypeService = secondFolder['foldername'],
            QualityService = firstFolder['foldername'],
            SKUService = obj.vendorpartnumber,
            DescriptionService = obj.description,
            priceService = obj.list,
            QtyService = 1,
        )
        if created == True:
            service.save()
            print(Service.object.all())
