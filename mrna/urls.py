from django.urls import path

from . import views

urlpatterns = [
    path('biological/', views.biological, name='mrna'),
    path('correlation/', views.correlation,name='mrna'),
    path('correlation/select/', views.select, name='mrna'),
    path('biological/bio_select/', views.bio_select, name='mrna'),
]