from django.db import models

# mapping of data to databases

# sets up Service model, main model
class Service(models.Model):
    ServiceTypeService = models.CharField(max_length = 100)
    TypeService= models.CharField(max_length = 100)
    QualityService = models.CharField(max_length = 100)
    SKUService = models.CharField(max_length = 50)
    DescriptionService = models.CharField(max_length = 200)
    priceService = models.FloatField()
    QtyService = models.IntegerField(default=1)

    def __str__(self):
        # requesting it gives you its description, useful for debugging
        return self.DescriptionService

class Quote(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(Service)


    def __str__(self):
        # requesting it gives you its description, useful for debugging
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

#function that merges the two table to actually useful stuff
def merge_models(apps, schema_editor):
    #gets all products
    for obj in ProductsCommerxcatalogProducts.objects.all():
        #just incase it doesn't work
        try:
            thirdFolder = 'Not Specified'
            secondFolder = 'Other'
            firstFolder = '-'
            #gets the products folderlist and using this find what categories it belongs to
            if(obj.folderlist is not None):
                #formats it and does away with all un acceptable inputs
                folderId = obj.folderlist.replace('(83)', '').replace('(84)', '').replace('(', '').replace(')', '')
                if (folderId != ''):
                    #set the quality to string found at the folderId
                    firstFolder = ProductsCommerxcatalogFolders.objects.filter(id = folderId).values()[0]
                    print(firstFolder)

                    #check to make sure there is actually a second folder
                    if(firstFolder['indentlevel'] > 2):
                        #using an attribute called parent id set the type to the string of the folder with that id
                        secondFolder = ProductsCommerxcatalogFolders.objects.filter(id = firstFolder['parentid']).values()[0]
                        print(secondFolder)
                    else:
                        secondFolder = firstFolder

                    #does the same thing as the secondFolder
                    thirdFolder = ProductsCommerxcatalogFolders.objects.filter(id = secondFolder['parentid']).values()[0]
                    print(thirdFolder)

                    #changes the default value
                    thirdFolder = thirdFolder['foldername']
                    secondFolder = secondFolder['foldername']
                    firstFolder = firstFolder['foldername']
        except:
            print("DIDNT WORK!")

        #create an object but if it already exist just do nothing

        service, created = Service.objects.get_or_create(
            ServiceTypeService = thirdFolder,
            TypeService = secondFolder,
            QualityService = firstFolder,
            SKUService = obj.vendorpartnumber,
            DescriptionService = obj.description,
            priceService = obj.list,
            QtyService = 1,
        )
        if created == True:
            #save it
            service.save()
            print(service)
