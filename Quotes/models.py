from django.db import models

# mapping of data to databases

class ProductsCommerxcatalogFolders(models.Model):
    foldername = models.CharField(db_column='FolderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    indentlevel = models.SmallIntegerField(db_column='IndentLevel', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Folders'

class ProductsCommerxcatalogProducts(models.Model):
    category = models.CharField(max_length = 100, db_column='Category')
    extralng01 = models.IntegerField(db_column='ExtraLng01', blank=True, null=True, default=1)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    folderlist = models.TextField(db_column='FolderList', blank=True, null=True)  # Field name made lowercase.
    list = models.FloatField(db_column='List', blank=True, null=True)  # Field name made lowercase.
    vendorpartnumber = models.CharField(db_column='VendorPartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(max_length = 100, db_column='ItemType')
    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Products'

class SavedQuotes(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(ProductsCommerxcatalogProducts)


    def __str__(self):
        # requesting it gives you its description, useful for debugging
        return self.Name
