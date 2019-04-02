from django.urls import path

from . import views

urlpatterns = [
    path('', views.process_url_from_client, name='index'),
    path('process_url_from_client/',views.the_new_one),
]