from django.urls import path

from . import views

urlpatterns = [
    path('specific/', views.specific, name='survival'),
    path('across/', views.across, name='survival'),
]