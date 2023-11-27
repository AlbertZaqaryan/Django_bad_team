from django.urls import path
from . import views

urlpatterns=[
    path('', views.category, name='category'),
    path('notebooks/<str:slug>/', views.notebooks, name='notebooks'),
]