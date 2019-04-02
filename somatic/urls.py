from django.urls import path

from . import views

urlpatterns = [
    path('', views.somatic, name='somatic'),
    path('select/', views.select, name='somatic'),

]