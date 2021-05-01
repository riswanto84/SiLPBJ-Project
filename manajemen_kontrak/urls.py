from django.urls import path
from . import views

urlpatterns = [
    
    path('master_template/', views.master_template, name='master_template'),
     path('under_contructions/', views.under_contructions, name='under_contructions'),

    # path untuk login admin 
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('home_dashboard', views.home_dashboard, name='home_dashboard'),
]