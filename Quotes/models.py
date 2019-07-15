from django.db import models

class Service(models.Model):
    ServiceType = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Quality = models.CharField(max_length = 100)
    SKU = models.CharField(db_column='VendorPartNumber', max_length = 20)
    Description = models.CharField(db_column='Description', max_length = 200)
    Price = models.FloatField(db_column='Cost')
    Qty = models.IntegerField(default=1)

    class Meta:
        db_table = 'Products_CommerxCatalog_Products'
    def __str__(self):
        return self.Description

class Quote(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(Service)


    def __str__(self):
        return self.Name
