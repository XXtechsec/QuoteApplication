from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('QuoteMaker', views.QuoteMaker, name='QuoteMaker'),
    path('result', views.result, name='result'),
    path('pdf', views.Pdf, name= 'Pdf'),
    path('CSV', views.CSV, name= 'CSV'),
    path('delete', views.delete, name= 'delete'),
    path('Qty', views.Qty, name= 'Qty'),
    path('changeQuality', views.changeQuality, name= 'changeQuality'),
    path('search', views.search, name= 'search'),
    path('select', views.select, name= 'select'),
    path('saveQuote', views.saveQuote, name= 'saveQuote'),
    path('logout/', views.logout, name='logout'),

]
