from django.contrib import admin
from Quotes.models import ProductsCommerxcatalogProducts
from Quotes.models import SavedQuotes

class ServiceAdmin(admin.ModelAdmin):
    # pass what attributes to display and what search field will look for in admin
    list_display = ('itemtype','description', 'list')
    search_fields = ('itemtype', 'description', 'vendorpartnumber', 'id' )
    pass
# register model for admin
admin.site.register(ProductsCommerxcatalogProducts, ServiceAdmin)

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('Name','Company')
    search_fields = ('Name','Company')
    pass
# register model for admin
admin.site.register(SavedQuotes, QuoteAdmin)
