from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('register/', views.register, name='register'),
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
    # add category
    path('quan-ly-danh-muc/add/', views.addUsertoCategory, name="addUsertoCategory"),
    path('addCategoryPost/', views.addCategoryPost, name="addCategoryPost"),
    #update category
    path('quan-ly-danh-muc/update/<str:id>/', views.updateCategory, name="updateCategory"),
    path('updateCategoryPost/', views.updateCategoryPost, name="updateCategoryPost"),
    path('quan-ly-danh-muc/search/<str:searchInput>/', views.searchCategory, name="searchCategory"),
    #delete category
    path('quan-ly-danh-muc/delete/<str:id>/', views.deleteCategory, name="deleteCategory"),
    path('quan-ly-sach/', views.quanlysach, name="quanlysach"),
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    #quan ly tinh hinh muon tra
    path('quan-ly-tinh-hinh-muon-tra/', views.quanlytinhhinhmuontra, name="quanlytinhhinhmuontra"),
    path('quan-ly-tinh-hinh-muon-tra/load-form', views.quanlytinhhinhDaTra, name="quanlytinhhinhDaTra"),

    path('quan-ly-kho-sach/', views.quanlykhosach, name="quanlykhosach"),
    path('logout/', views.logout, name="logout"),
    # Form action submit
    path('loginPost/', views.loginPost, name='loginPost'),
    path('registerPost/', views.registerPost, name='registerPost'),
]