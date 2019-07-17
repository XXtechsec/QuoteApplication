# Generated by Django 2.1 on 2019-07-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes', '0005_auto_20190715_1608'),
    ]


    operations = [
        migrations.CreateModel(
            name='ProductsCommerxcatalogFolders',
            fields=[
                ('extradate01', models.DateTimeField(blank=True, db_column='ExtraDate01', null=True)),
                ('extradbl01', models.FloatField(blank=True, db_column='ExtraDbl01', null=True)),
                ('extralng01', models.IntegerField(blank=True, db_column='ExtraLng01', null=True)),
                ('extralogic01', models.BooleanField(blank=True, db_column='ExtraLogic01', null=True)),
                ('extramemo01', models.TextField(blank=True, db_column='ExtraMemo01', null=True)),
                ('extratext01', models.CharField(blank=True, db_column='ExtraText01', max_length=255, null=True)),
                ('extratext02', models.CharField(blank=True, db_column='ExtraText02', max_length=255, null=True)),
                ('foldername', models.CharField(blank=True, db_column='FolderName', max_length=255, null=True)),
                ('foldertype', models.CharField(blank=True, db_column='FolderType', max_length=20, null=True)),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('indentlevel', models.SmallIntegerField(blank=True, db_column='IndentLevel', null=True)),
                ('parentid', models.IntegerField(blank=True, db_column='ParentID', null=True)),
                ('ref1', models.CharField(blank=True, db_column='Ref1', max_length=255, null=True)),
                ('ref2', models.CharField(blank=True, db_column='Ref2', max_length=255, null=True)),
                ('ref3', models.CharField(blank=True, db_column='Ref3', max_length=255, null=True)),
                ('replicationid', models.CharField(blank=True, db_column='ReplicationID', max_length=36, null=True)),
            ],
            options={
                'db_table': 'Products_CommerxCatalog_Folders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductsCommerxcatalogProducts',
            fields=[
                ('accountingitemtype', models.CharField(blank=True, db_column='AccountingItemType', max_length=50, null=True)),
                ('accountingsalesaccount', models.CharField(blank=True, db_column='AccountingSalesAccount', max_length=50, null=True)),
                ('alternatecost', models.FloatField(blank=True, db_column='AlternateCost', null=True)),
                ('alternatecurrency', models.CharField(blank=True, db_column='AlternateCurrency', max_length=50, null=True)),
                ('alternatelist', models.FloatField(blank=True, db_column='AlternateList', null=True)),
                ('alternateprice', models.FloatField(blank=True, db_column='AlternatePrice', null=True)),
                ('availability', models.IntegerField(blank=True, db_column='Availability', null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=30, null=True)),
                ('commissionprofile', models.CharField(blank=True, db_column='CommissionProfile', max_length=30, null=True)),
                ('cost', models.FloatField(blank=True, db_column='Cost', null=True)),
                ('costandpricehistory', models.TextField(blank=True, db_column='CostAndPriceHistory', null=True)),
                ('costinglevel01', models.CharField(blank=True, db_column='CostingLevel01', max_length=100, null=True)),
                ('costinglevel02', models.CharField(blank=True, db_column='CostingLevel02', max_length=100, null=True)),
                ('costinglevel03', models.CharField(blank=True, db_column='CostingLevel03', max_length=100, null=True)),
                ('costinglevel04', models.CharField(blank=True, db_column='CostingLevel04', max_length=100, null=True)),
                ('costinglevel05', models.CharField(blank=True, db_column='CostingLevel05', max_length=100, null=True)),
                ('costinglevel06', models.CharField(blank=True, db_column='CostingLevel06', max_length=100, null=True)),
                ('costinglevel07', models.CharField(blank=True, db_column='CostingLevel07', max_length=100, null=True)),
                ('costinglevel08', models.CharField(blank=True, db_column='CostingLevel08', max_length=100, null=True)),
                ('costinglevel09', models.CharField(blank=True, db_column='CostingLevel09', max_length=100, null=True)),
                ('costinglevel10', models.CharField(blank=True, db_column='CostingLevel10', max_length=100, null=True)),
                ('costinglevel11', models.CharField(blank=True, db_column='CostingLevel11', max_length=100, null=True)),
                ('costinglevel12', models.CharField(blank=True, db_column='CostingLevel12', max_length=100, null=True)),
                ('costinglevel13', models.CharField(blank=True, db_column='CostingLevel13', max_length=100, null=True)),
                ('costinglevel14', models.CharField(blank=True, db_column='CostingLevel14', max_length=100, null=True)),
                ('costinglevel15', models.CharField(blank=True, db_column='CostingLevel15', max_length=100, null=True)),
                ('costmodifier', models.CharField(blank=True, db_column='CostModifier', max_length=18, null=True)),
                ('created', models.DateTimeField(blank=True, db_column='Created', null=True)),
                ('customdate01', models.DateTimeField(blank=True, db_column='CustomDate01', null=True)),
                ('customdate02', models.DateTimeField(blank=True, db_column='CustomDate02', null=True)),
                ('customdate03', models.DateTimeField(blank=True, db_column='CustomDate03', null=True)),
                ('customdate04', models.DateTimeField(blank=True, db_column='CustomDate04', null=True)),
                ('customdate05', models.DateTimeField(blank=True, db_column='CustomDate05', null=True)),
                ('custommemo01', models.TextField(blank=True, db_column='CustomMemo01', null=True)),
                ('custommemo02', models.TextField(blank=True, db_column='CustomMemo02', null=True)),
                ('custommemo03', models.TextField(blank=True, db_column='CustomMemo03', null=True)),
                ('custommemo04', models.TextField(blank=True, db_column='CustomMemo04', null=True)),
                ('custommemo05', models.TextField(blank=True, db_column='CustomMemo05', null=True)),
                ('customnumber01', models.FloatField(blank=True, db_column='CustomNumber01', null=True)),
                ('customnumber02', models.FloatField(blank=True, db_column='CustomNumber02', null=True)),
                ('customnumber03', models.FloatField(blank=True, db_column='CustomNumber03', null=True)),
                ('customnumber04', models.FloatField(blank=True, db_column='CustomNumber04', null=True)),
                ('customnumber05', models.FloatField(blank=True, db_column='CustomNumber05', null=True)),
                ('customtext01', models.CharField(blank=True, db_column='CustomText01', max_length=255, null=True)),
                ('customtext02', models.CharField(blank=True, db_column='CustomText02', max_length=255, null=True)),
                ('customtext03', models.CharField(blank=True, db_column='CustomText03', max_length=255, null=True)),
                ('customtext04', models.CharField(blank=True, db_column='CustomText04', max_length=255, null=True)),
                ('customtext05', models.CharField(blank=True, db_column='CustomText05', max_length=255, null=True)),
                ('customtext06', models.CharField(blank=True, db_column='CustomText06', max_length=255, null=True)),
                ('customtext07', models.CharField(blank=True, db_column='CustomText07', max_length=255, null=True)),
                ('customtext08', models.CharField(blank=True, db_column='CustomText08', max_length=255, null=True)),
                ('customtext09', models.CharField(blank=True, db_column='CustomText09', max_length=255, null=True)),
                ('customtext10', models.CharField(blank=True, db_column='CustomText10', max_length=255, null=True)),
                ('customtext11', models.CharField(blank=True, db_column='CustomText11', max_length=255, null=True)),
                ('customtext12', models.CharField(blank=True, db_column='CustomText12', max_length=255, null=True)),
                ('customtext13', models.CharField(blank=True, db_column='CustomText13', max_length=255, null=True)),
                ('customtext14', models.CharField(blank=True, db_column='CustomText14', max_length=255, null=True)),
                ('customtext15', models.CharField(blank=True, db_column='CustomText15', max_length=255, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('discontinued', models.BooleanField(blank=True, db_column='Discontinued', null=True)),
                ('extendeddescription', models.TextField(blank=True, db_column='ExtendedDescription', null=True)),
                ('extradate01', models.DateTimeField(blank=True, db_column='ExtraDate01', null=True)),
                ('extradbl01', models.FloatField(blank=True, db_column='ExtraDbl01', null=True)),
                ('extralng01', models.IntegerField(blank=True, db_column='ExtraLng01', null=True)),
                ('extralogic01', models.BooleanField(blank=True, db_column='ExtraLogic01', null=True)),
                ('extramemo01', models.TextField(blank=True, db_column='ExtraMemo01', null=True)),
                ('extratext01', models.CharField(blank=True, db_column='ExtraText01', max_length=255, null=True)),
                ('extratext02', models.CharField(blank=True, db_column='ExtraText02', max_length=255, null=True)),
                ('folderlist', models.TextField(blank=True, db_column='FolderList', null=True)),
                ('formula', models.TextField(blank=True, db_column='Formula', null=True)),
                ('grouptag', models.CharField(blank=True, db_column='GroupTag', max_length=30, null=True)),
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('internaldescription', models.TextField(blank=True, db_column='InternalDescription', null=True)),
                ('internalpartnumber', models.CharField(blank=True, db_column='InternalPartNumber', max_length=255, null=True)),
                ('itemtype', models.CharField(blank=True, db_column='ItemType', max_length=30, null=True)),
                ('keywordlist', models.CharField(blank=True, db_column='KeywordList', max_length=255, null=True)),
                ('lastmodified', models.DateTimeField(blank=True, db_column='LastModified', null=True)),
                ('lastmodifiedby', models.CharField(blank=True, db_column='LastModifiedBy', max_length=40, null=True)),
                ('lineitemattributes', models.IntegerField(blank=True, db_column='LineItemAttributes', null=True)),
                ('lineitemtype', models.IntegerField(blank=True, db_column='LineItemType', null=True)),
                ('list', models.FloatField(blank=True, db_column='List', null=True)),
                ('manufacturer', models.CharField(blank=True, db_column='Manufacturer', max_length=40, null=True)),
                ('manufacturerpartnumber', models.CharField(blank=True, db_column='ManufacturerPartNumber', max_length=40, null=True)),
                ('notes', models.CharField(blank=True, db_column='Notes', max_length=255, null=True)),
                ('picturefilename', models.CharField(blank=True, db_column='PictureFileName', max_length=255, null=True)),
                ('price', models.FloatField(blank=True, db_column='Price', null=True)),
                ('pricemodifier', models.CharField(blank=True, db_column='PriceModifier', max_length=18, null=True)),
                ('priceprofile', models.CharField(blank=True, db_column='PriceProfile', max_length=50, null=True)),
                ('pricinglastupdated', models.DateTimeField(blank=True, db_column='PricingLastUpdated', null=True)),
                ('pricinglevel01', models.CharField(blank=True, db_column='PricingLevel01', max_length=100, null=True)),
                ('pricinglevel02', models.CharField(blank=True, db_column='PricingLevel02', max_length=100, null=True)),
                ('pricinglevel03', models.CharField(blank=True, db_column='PricingLevel03', max_length=100, null=True)),
                ('pricinglevel04', models.CharField(blank=True, db_column='PricingLevel04', max_length=100, null=True)),
                ('pricinglevel05', models.CharField(blank=True, db_column='PricingLevel05', max_length=100, null=True)),
                ('pricinglevel06', models.CharField(blank=True, db_column='PricingLevel06', max_length=100, null=True)),
                ('pricinglevel07', models.CharField(blank=True, db_column='PricingLevel07', max_length=100, null=True)),
                ('pricinglevel08', models.CharField(blank=True, db_column='PricingLevel08', max_length=100, null=True)),
                ('pricinglevel09', models.CharField(blank=True, db_column='PricingLevel09', max_length=100, null=True)),
                ('pricinglevel10', models.CharField(blank=True, db_column='PricingLevel10', max_length=100, null=True)),
                ('pricinglevel11', models.CharField(blank=True, db_column='PricingLevel11', max_length=100, null=True)),
                ('pricinglevel12', models.CharField(blank=True, db_column='PricingLevel12', max_length=100, null=True)),
                ('pricinglevel13', models.CharField(blank=True, db_column='PricingLevel13', max_length=100, null=True)),
                ('pricinglevel14', models.CharField(blank=True, db_column='PricingLevel14', max_length=100, null=True)),
                ('pricinglevel15', models.CharField(blank=True, db_column='PricingLevel15', max_length=100, null=True)),
                ('printpicture', models.BooleanField(blank=True, db_column='PrintPicture', null=True)),
                ('qtymultiplier1', models.FloatField(blank=True, db_column='QtyMultiplier1', null=True)),
                ('qtymultiplier2', models.FloatField(blank=True, db_column='QtyMultiplier2', null=True)),
                ('qtymultiplier3', models.FloatField(blank=True, db_column='QtyMultiplier3', null=True)),
                ('qtymultiplier4', models.FloatField(blank=True, db_column='QtyMultiplier4', null=True)),
                ('quickserviceinfo', models.TextField(blank=True, db_column='QuickServiceInfo', null=True)),
                ('replicationid', models.CharField(blank=True, db_column='ReplicationID', max_length=36, null=True)),
                ('serialnumber', models.CharField(blank=True, db_column='SerialNumber', max_length=35, null=True)),
                ('shortdescription', models.CharField(blank=True, db_column='ShortDescription', max_length=255, null=True)),
                ('specsheetname', models.CharField(blank=True, db_column='SpecSheetName', max_length=255, null=True)),
                ('taxcode', models.CharField(blank=True, db_column='TaxCode', max_length=1, null=True)),
                ('taxrate', models.FloatField(blank=True, db_column='TaxRate', null=True)),
                ('unitofmeasure', models.CharField(blank=True, db_column='UnitOfMeasure', max_length=12, null=True)),
                ('unitofmeasurefactor', models.FloatField(blank=True, db_column='UnitOfMeasureFactor', null=True)),
                ('unitofpricing', models.CharField(blank=True, db_column='UnitOfPricing', max_length=12, null=True)),
                ('unitofpricingfactor', models.FloatField(blank=True, db_column='UnitOfPricingFactor', null=True)),
                ('unitweight', models.FloatField(blank=True, db_column='UnitWeight', null=True)),
                ('vendor', models.CharField(blank=True, db_column='Vendor', max_length=50, null=True)),
                ('vendorpartnumber', models.CharField(blank=True, db_column='VendorPartNumber', max_length=40, null=True)),
                ('videourldata', models.TextField(blank=True, db_column='VideoURLData', null=True)),
                ('labordata', models.TextField(blank=True, db_column='LaborData', null=True)),
                ('shippingprice', models.FloatField(blank=True, db_column='ShippingPrice', null=True)),
                ('customtext16', models.CharField(blank=True, db_column='CustomText16', max_length=255, null=True)),
                ('customtext17', models.CharField(blank=True, db_column='CustomText17', max_length=255, null=True)),
                ('customtext18', models.CharField(blank=True, db_column='CustomText18', max_length=255, null=True)),
                ('customtext19', models.CharField(blank=True, db_column='CustomText19', max_length=255, null=True)),
                ('customtext20', models.CharField(blank=True, db_column='CustomText20', max_length=255, null=True)),
            ],
            options={
                'db_table': 'Products_CommerxCatalog_Products',
                'managed': False,
            },
        ),
    ]
