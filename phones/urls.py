from django.urls import path
from . import views

urlpatterns = [
    path('', views.phone_list, name='catalog_list'),
    path('<slug:slug>/', views.phone_detail, name='phone_detail'),
]


