from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('sign/',views.sign,name='sign'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

]