from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('home/', views.home, name="home"),
    path('quan-ly-nguoi-dung/', views.quanlynguoidung, name="quanlynguoidung"),
    path('quan-ly-danh-muc/', views.quanlydanhmuc, name="quanlydanhmuc"),
    path('quan-ly-sach/', views.quanlysach, name="quanlysach"),
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    path('quan-ly-tinh-hinh-muon-tra/', views.quanlytinhhinhmuontra, name="quanlytinhhinhmuontra"),
    path('quan-ly-kho-sach/', views.quanlykhosach, name="quanlykhosach"),
    path('logout/', views.logout, name="logout"),
    # Form action submit
    path('loginPost/', views.loginPost, name='loginPost'),
]