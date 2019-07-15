from django.contrib import admin
from Quotes.models import Service
from Quotes.models import Quote

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('TypeService','DescriptionService', 'priceService')
    search_fields = ('TypeService', 'DescriptionService', 'SKUService', 'id' )
    pass
admin.site.register(Service, ServiceAdmin)

class QuoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Quote, QuoteAdmin)
