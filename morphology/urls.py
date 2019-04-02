from django.urls import path

from . import views

urlpatterns = [
    path('', views.feature_extraction, name='morphology'),
    path('feature_distribution/', views.feature_distribution,name='morphology'),
    path('feature_distribution/search/', views.search, name='morphology'),
]