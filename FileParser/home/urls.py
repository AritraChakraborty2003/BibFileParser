from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name="index"),
    path('arvix',views.aravix,name="arvix")

]