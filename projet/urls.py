from django.urls import path,include
from django.contrib import admin
urlpatterns = [

    path('admin/',admin.site.urls),
    path('',include('produit.urls')),
    path('commande',include('commande.urls')),
    path('client',include('client.urls')),



]
