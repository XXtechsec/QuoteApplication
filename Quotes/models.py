from django.db import models

class Service(models.Model):
    ServiceType = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Quality = models.CharField(max_length = 100)
    SKU = models.CharField(max_length = 20)
    Description = models.CharField(max_length = 200)
    price = models.FloatField()
    Qty = models.IntegerField(default=1)

    def __str__(self):
        return self.Description

class Quote(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(Service)


    def __str__(self):
        return self.Name


class ProductsCommerxcatalogFolders(models.Model):
    extradate01 = models.DateTimeField(db_column='ExtraDate01', blank=True, null=True)  # Field name made lowercase.
    extradbl01 = models.FloatField(db_column='ExtraDbl01', blank=True, null=True)  # Field name made lowercase.
    extralng01 = models.IntegerField(db_column='ExtraLng01', blank=True, null=True)  # Field name made lowercase.
    extralogic01 = models.BooleanField(db_column='ExtraLogic01', blank=True, null=True)  # Field name made lowercase.
    extramemo01 = models.TextField(db_column='ExtraMemo01', blank=True, null=True)  # Field name made lowercase.
    extratext01 = models.CharField(db_column='ExtraText01', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extratext02 = models.CharField(db_column='ExtraText02', max_length=255, blank=True, null=True)  # Field name made lowercase.
    foldername = models.CharField(db_column='FolderName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    foldertype = models.CharField(db_column='FolderType', max_length=20, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    indentlevel = models.SmallIntegerField(db_column='IndentLevel', blank=True, null=True)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID', blank=True, null=True)  # Field name made lowercase.
    ref1 = models.CharField(db_column='Ref1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref2 = models.CharField(db_column='Ref2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ref3 = models.CharField(db_column='Ref3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    replicationid = models.CharField(db_column='ReplicationID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Folders'

class ProductsCommerxcatalogProducts(models.Model):
    accountingitemtype = models.CharField(db_column='AccountingItemType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    accountingsalesaccount = models.CharField(db_column='AccountingSalesAccount', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alternatecost = models.FloatField(db_column='AlternateCost', blank=True, null=True)  # Field name made lowercase.
    alternatecurrency = models.CharField(db_column='AlternateCurrency', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alternatelist = models.FloatField(db_column='AlternateList', blank=True, null=True)  # Field name made lowercase.
    alternateprice = models.FloatField(db_column='AlternatePrice', blank=True, null=True)  # Field name made lowercase.
    availability = models.IntegerField(db_column='Availability', blank=True, null=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=30, blank=True, null=True)  # Field name made lowercase.
    commissionprofile = models.CharField(db_column='CommissionProfile', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    costandpricehistory = models.TextField(db_column='CostAndPriceHistory', blank=True, null=True)  # Field name made lowercase.
    costinglevel01 = models.CharField(db_column='CostingLevel01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel02 = models.CharField(db_column='CostingLevel02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel03 = models.CharField(db_column='CostingLevel03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel04 = models.CharField(db_column='CostingLevel04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel05 = models.CharField(db_column='CostingLevel05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel06 = models.CharField(db_column='CostingLevel06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel07 = models.CharField(db_column='CostingLevel07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel08 = models.CharField(db_column='CostingLevel08', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel09 = models.CharField(db_column='CostingLevel09', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel10 = models.CharField(db_column='CostingLevel10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel11 = models.CharField(db_column='CostingLevel11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel12 = models.CharField(db_column='CostingLevel12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel13 = models.CharField(db_column='CostingLevel13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel14 = models.CharField(db_column='CostingLevel14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costinglevel15 = models.CharField(db_column='CostingLevel15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    costmodifier = models.CharField(db_column='CostModifier', max_length=18, blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)  # Field name made lowercase.
    customdate01 = models.DateTimeField(db_column='CustomDate01', blank=True, null=True)  # Field name made lowercase.
    customdate02 = models.DateTimeField(db_column='CustomDate02', blank=True, null=True)  # Field name made lowercase.
    customdate03 = models.DateTimeField(db_column='CustomDate03', blank=True, null=True)  # Field name made lowercase.
    customdate04 = models.DateTimeField(db_column='CustomDate04', blank=True, null=True)  # Field name made lowercase.
    customdate05 = models.DateTimeField(db_column='CustomDate05', blank=True, null=True)  # Field name made lowercase.
    custommemo01 = models.TextField(db_column='CustomMemo01', blank=True, null=True)  # Field name made lowercase.
    custommemo02 = models.TextField(db_column='CustomMemo02', blank=True, null=True)  # Field name made lowercase.
    custommemo03 = models.TextField(db_column='CustomMemo03', blank=True, null=True)  # Field name made lowercase.
    custommemo04 = models.TextField(db_column='CustomMemo04', blank=True, null=True)  # Field name made lowercase.
    custommemo05 = models.TextField(db_column='CustomMemo05', blank=True, null=True)  # Field name made lowercase.
    customnumber01 = models.FloatField(db_column='CustomNumber01', blank=True, null=True)  # Field name made lowercase.
    customnumber02 = models.FloatField(db_column='CustomNumber02', blank=True, null=True)  # Field name made lowercase.
    customnumber03 = models.FloatField(db_column='CustomNumber03', blank=True, null=True)  # Field name made lowercase.
    customnumber04 = models.FloatField(db_column='CustomNumber04', blank=True, null=True)  # Field name made lowercase.
    customnumber05 = models.FloatField(db_column='CustomNumber05', blank=True, null=True)  # Field name made lowercase.
    customtext01 = models.CharField(db_column='CustomText01', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext02 = models.CharField(db_column='CustomText02', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext03 = models.CharField(db_column='CustomText03', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext04 = models.CharField(db_column='CustomText04', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext05 = models.CharField(db_column='CustomText05', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext06 = models.CharField(db_column='CustomText06', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext07 = models.CharField(db_column='CustomText07', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext08 = models.CharField(db_column='CustomText08', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext09 = models.CharField(db_column='CustomText09', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext10 = models.CharField(db_column='CustomText10', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext11 = models.CharField(db_column='CustomText11', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext12 = models.CharField(db_column='CustomText12', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext13 = models.CharField(db_column='CustomText13', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext14 = models.CharField(db_column='CustomText14', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext15 = models.CharField(db_column='CustomText15', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    discontinued = models.BooleanField(db_column='Discontinued', blank=True, null=True)  # Field name made lowercase.
    extendeddescription = models.TextField(db_column='ExtendedDescription', blank=True, null=True)  # Field name made lowercase.
    extradate01 = models.DateTimeField(db_column='ExtraDate01', blank=True, null=True)  # Field name made lowercase.
    extradbl01 = models.FloatField(db_column='ExtraDbl01', blank=True, null=True)  # Field name made lowercase.
    extralng01 = models.IntegerField(db_column='ExtraLng01', blank=True, null=True)  # Field name made lowercase.
    extralogic01 = models.BooleanField(db_column='ExtraLogic01', blank=True, null=True)  # Field name made lowercase.
    extramemo01 = models.TextField(db_column='ExtraMemo01', blank=True, null=True)  # Field name made lowercase.
    extratext01 = models.CharField(db_column='ExtraText01', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extratext02 = models.CharField(db_column='ExtraText02', max_length=255, blank=True, null=True)  # Field name made lowercase.
    folderlist = models.TextField(db_column='FolderList', blank=True, null=True)  # Field name made lowercase.
    formula = models.TextField(db_column='Formula', blank=True, null=True)  # Field name made lowercase.
    grouptag = models.CharField(db_column='GroupTag', max_length=30, blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    internaldescription = models.TextField(db_column='InternalDescription', blank=True, null=True)  # Field name made lowercase.
    internalpartnumber = models.CharField(db_column='InternalPartNumber', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=30, blank=True, null=True)  # Field name made lowercase.
    keywordlist = models.CharField(db_column='KeywordList', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastmodified = models.DateTimeField(db_column='LastModified', blank=True, null=True)  # Field name made lowercase.
    lastmodifiedby = models.CharField(db_column='LastModifiedBy', max_length=40, blank=True, null=True)  # Field name made lowercase.
    lineitemattributes = models.IntegerField(db_column='LineItemAttributes', blank=True, null=True)  # Field name made lowercase.
    lineitemtype = models.IntegerField(db_column='LineItemType', blank=True, null=True)  # Field name made lowercase.
    list = models.FloatField(db_column='List', blank=True, null=True)  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=40, blank=True, null=True)  # Field name made lowercase.
    manufacturerpartnumber = models.CharField(db_column='ManufacturerPartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    picturefilename = models.CharField(db_column='PictureFileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    priceService = models.FloatField(db_column='Price')  # Field name made lowercase.
    pricemodifier = models.CharField(db_column='PriceModifier', max_length=18, blank=True, null=True)  # Field name made lowercase.
    priceprofile = models.CharField(db_column='PriceProfile', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pricinglastupdated = models.DateTimeField(db_column='PricingLastUpdated', blank=True, null=True)  # Field name made lowercase.
    pricinglevel01 = models.CharField(db_column='PricingLevel01', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel02 = models.CharField(db_column='PricingLevel02', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel03 = models.CharField(db_column='PricingLevel03', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel04 = models.CharField(db_column='PricingLevel04', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel05 = models.CharField(db_column='PricingLevel05', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel06 = models.CharField(db_column='PricingLevel06', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel07 = models.CharField(db_column='PricingLevel07', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel08 = models.CharField(db_column='PricingLevel08', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel09 = models.CharField(db_column='PricingLevel09', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel10 = models.CharField(db_column='PricingLevel10', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel11 = models.CharField(db_column='PricingLevel11', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel12 = models.CharField(db_column='PricingLevel12', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel13 = models.CharField(db_column='PricingLevel13', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel14 = models.CharField(db_column='PricingLevel14', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pricinglevel15 = models.CharField(db_column='PricingLevel15', max_length=100, blank=True, null=True)  # Field name made lowercase.
    printpicture = models.BooleanField(db_column='PrintPicture', blank=True, null=True)  # Field name made lowercase.
    qtymultiplier1 = models.FloatField(db_column='QtyMultiplier1', blank=True, null=True)  # Field name made lowercase.
    qtymultiplier2 = models.FloatField(db_column='QtyMultiplier2', blank=True, null=True)  # Field name made lowercase.
    qtymultiplier3 = models.FloatField(db_column='QtyMultiplier3', blank=True, null=True)  # Field name made lowercase.
    qtymultiplier4 = models.FloatField(db_column='QtyMultiplier4', blank=True, null=True)  # Field name made lowercase.
    quickserviceinfo = models.TextField(db_column='QuickServiceInfo', blank=True, null=True)  # Field name made lowercase.
    replicationid = models.CharField(db_column='ReplicationID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    serialnumber = models.CharField(db_column='SerialNumber', max_length=35, blank=True, null=True)  # Field name made lowercase.
    shortdescription = models.CharField(db_column='ShortDescription', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specsheetname = models.CharField(db_column='SpecSheetName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taxcode = models.CharField(db_column='TaxCode', max_length=1, blank=True, null=True)  # Field name made lowercase.
    taxrate = models.FloatField(db_column='TaxRate', blank=True, null=True)  # Field name made lowercase.
    unitofmeasure = models.CharField(db_column='UnitOfMeasure', max_length=12, blank=True, null=True)  # Field name made lowercase.
    unitofmeasurefactor = models.FloatField(db_column='UnitOfMeasureFactor', blank=True, null=True)  # Field name made lowercase.
    unitofpricing = models.CharField(db_column='UnitOfPricing', max_length=12, blank=True, null=True)  # Field name made lowercase.
    unitofpricingfactor = models.FloatField(db_column='UnitOfPricingFactor', blank=True, null=True)  # Field name made lowercase.
    unitweight = models.FloatField(db_column='UnitWeight', blank=True, null=True)  # Field name made lowercase.
    vendor = models.CharField(db_column='Vendor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    vendorpartnumber = models.CharField(db_column='VendorPartNumber', max_length=40, blank=True, null=True)  # Field name made lowercase.
    videourldata = models.TextField(db_column='VideoURLData', blank=True, null=True)  # Field name made lowercase.
    labordata = models.TextField(db_column='LaborData', blank=True, null=True)  # Field name made lowercase.
    shippingprice = models.FloatField(db_column='ShippingPrice', blank=True, null=True)  # Field name made lowercase.
    customtext16 = models.CharField(db_column='CustomText16', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext17 = models.CharField(db_column='CustomText17', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext18 = models.CharField(db_column='CustomText18', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext19 = models.CharField(db_column='CustomText19', max_length=255, blank=True, null=True)  # Field name made lowercase.
    customtext20 = models.CharField(db_column='CustomText20', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products_CommerxCatalog_Products'

def merge_models(apps, schema_editor):
    for obj in ProductsCommerxcatalogProducts.objects.all():
        firstFolder = ProductsCommerxcatalogFolders.objects.filter(id = obj.folderlist.replace('(', '').replace(')', '')).values()[0]
        secondFolder = ProductsCommerxcatalogFolders.objects.filter(id = firstFolder['parentid']).values()[0]
        thirdFolder = ProductsCommerxcatalogFolders.objects.filter(id = secondFolder['parentid']).values()[0]

        service, created = Service.objects.get_or_create(
            ServiceType = thirdFolder['foldername'],
            Type = secondFolder['foldername'],
            Quality = firstFolder['foldername'],
            SKU = obj.vendorpartnumber,
            Description = obj.description,
            Price = obj.list,
            Qty = 1,
        )
