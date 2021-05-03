from django.urls import path
from . import views

urlpatterns = [
    
    path('master_template/', views.master_template, name='master_template'),
     path('under_contructions/', views.under_contructions, name='under_contructions'),

    # path untuk login admin 
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logoutUser, name='logout'),
    path('home_dashboard', views.home_dashboard, name='home_dashboard'),

    # path untuk use case entry barang
    path('EntryBarang/', views.EntryBarang, name='EntryBarang'),
    path('detail_barang/<str:pk>', views.detail_barang, name='detail_barang'),
    path('ubah_barang/<str:pk>', views.ubah_barang, name='ubah_barang'),
    path('hapus_barang/<str:pk>', views.hapus_barang, name='hapus_barang'),

    # path untuk use case entry penyedia
    path('EntryPenyedia/', views.EntryPenyedia, name='EntryPenyedia'),
    path('detail_penyedia/<str:pk>', views.detail_penyedia, name='detail_penyedia'),
    path('ubah_penyedia/<str:pk>', views.ubah_penyedia, name='ubah_penyedia'),
    path('hapus_penyedia/<str:pk>', views.hapus_penyedia, name='hapus_penyedia'),
]