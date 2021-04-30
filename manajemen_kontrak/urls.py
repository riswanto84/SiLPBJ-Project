from django.urls import path
from . import views

urlpatterns = [
    # path untuk login admin
    path('login/', views.login_page, name='login_page'),
    path('home_dashboard', views.home_dashboard, name='home_dashboard'),
]