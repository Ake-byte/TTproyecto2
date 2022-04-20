from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('registros/', views.getRegistros, name="registros"),
    path('registros/<str:pk>/', views.getRegistro, name="registro"),
]