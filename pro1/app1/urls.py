from django.contrib import admin
from django.urls import path
from app1 import views
app_name="pypo"
urlpatterns = [
    path('',views.display)
]
