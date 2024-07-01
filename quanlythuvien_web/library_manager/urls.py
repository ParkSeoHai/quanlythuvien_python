from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('home/', views.home, name="home"),
    # Url quan ly nguoi dung
    path('quan-ly-nguoi-dung/', views.quanlynguoidung, name="quanlynguoidung"),
    # Add user
    path('quan-ly-nguoi-dung/add/', views.addUser, name="addUser"),
    path('addUserPost/', views.addUserPost, name="addUserPost"),
    # Update user
    path('quan-ly-nguoi-dung/update/<str:id>/', views.updateUser, name="updateUser"),
    path('updateUserPost/', views.updateUserPost, name="updateUserPost"),
    # Delete user
    path('quan-ly-nguoi-dung/delete/<str:id>/', views.deleteUser, name="deleteUser"),
    # Search user
    path('quan-ly-nguoi-dung/search/<str:searchInput>/', views.searchUser, name="searchUser"),

    # Quan ly danh muc
    path('quan-ly-danh-muc/', views.quanlydanhmuc, name="quanlydanhmuc"),
    path('quan-ly-sach/', views.quanlysach, name="quanlysach"),
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    path('quan-ly-tinh-hinh-muon-tra/', views.quanlytinhhinhmuontra, name="quanlytinhhinhmuontra"),
    
    # Quan ly kho sach
    # path('quan-ly-kho-sach/', views.quanlykhosach, name="quanlykhosach"),
    path('getBookById/', views.getBook, name="getBook"),

    # Quan ly kho sach - nhap sach
    path('quan-ly-kho-sach/nhap-sach/', views.nhapsach, name="nhapsachIndex"),
    # Lap phieu nhap sach
    path('quan-ly-kho-sach/nhap-sach/add/', views.addPhieunhap, name="addPhieunhap"),
    # Cap nhat phieu nhap sach
    path('quan-ly-kho-sach/nhap-sach/update/<str:id>/', views.updatePhieunhap, name="updatePhieunhap"),
    # Info phieu nhap sach
    path('quan-ly-kho-sach/nhap-sach/info/<str:id>/', views.infoPhieunhap, name="infoPhieunhap"),
    # Post request nhap sach
    path('nhapsachPost/', views.nhapsachPost, name="nhapsachPost"),
    # Post request cap nhat phieu nhap
    path('updatePhieunhapPost/', views.updatePhieunhapPost, name="updatePhieunhapPost"),
    # Delete phieu nhap
    path('quan-ly-kho-sach/nhap-sach/delete/<str:id>/', views.deletePhieunhap, name="deletePhieunhap"),
    # Search phieu nhap by date
    path('quan-ly-kho-sach/nhap-sach/search/<str:dateFrom>/<str:dateTo>/', views.searchPhieunhapByDate, name="searchPhieunhapByDate"),

    path('logout/', views.logout, name="logout"),
    # Form action submit
    path('loginPost/', views.loginPost, name='loginPost'),
]