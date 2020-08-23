from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.film_people_list),
]