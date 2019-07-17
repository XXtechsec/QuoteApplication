from django.contrib import admin
from Quotes.models import ProductsCommerxcatalogProducts
from Quotes.models import Quote

class ServiceAdmin(admin.ModelAdmin):
    # pass what attributes to display and what search field will look for in admin
    list_display = ('vendorpartnumber','description', 'list')
    search_fields = ('vendorpartnumber', 'description', 'vendorpartnumber', 'id' )
    pass
# register model for admin
admin.site.register(ProductsCommerxcatalogProducts, ServiceAdmin)

class QuoteAdmin(admin.ModelAdmin):
    # add whatever you want here
    pass
# register model for admin
admin.site.register(Quote, QuoteAdmin)
