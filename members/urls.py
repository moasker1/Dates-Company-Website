from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('product/', views.product, name='product'),
    path("register/", views.register, name="register"),
    path('login/', views.login, name='login'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('logout/', views.logout, name='logout'),

] 