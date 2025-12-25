from django.urls import path
import phones
from . import views

urlpatterns = [
    path('', views.catalog_view, name='catalog_list'),
    path('<slug:slug>/', views.phone_detail_view, name='phone_detail'),
]