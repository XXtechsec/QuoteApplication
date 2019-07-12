from django.contrib import admin
from Quotes.models import Service
from Quotes.models import Quote

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Type','Description', 'Price')
    search_fields = ('Type', 'Description', 'SKU', 'id' )
    pass
admin.site.register(Service, ServiceAdmin)

class QuoteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Quote, QuoteAdmin)
