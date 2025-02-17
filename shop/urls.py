
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='Aboutus'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='TrakingStatus'),
    path('productview/', views.prodview, name='Search'),
    path('checkout/', views.checkout, name='Checkout'),
]
