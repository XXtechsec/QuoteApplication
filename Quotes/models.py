from django.db import models

class Service(models.Model):
    ServiceType = models.CharField(max_length = 100)
    Type = models.CharField(max_length = 100)
    Quality = models.CharField(max_length = 100)
    SKU = models.CharField(max_length = 20)
    Description = models.CharField(max_length = 200)
    Price = models.FloatField()
    Qty = models.IntegerField()

    def __str__(self):
        return self.Description

class Quote(models.Model):
    Name = models.CharField(max_length = 25)
    Company = models.CharField(max_length = 25)
    Contact = models.CharField(max_length = 25)
    Services = models.ManyToManyField(Service)


    def __str__(self):
        return self.Name
