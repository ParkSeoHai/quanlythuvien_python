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
    #url quan ly sach
    path('quan-ly-sach/', views.quanlysach, name="quanlysach"),
    #add sachs
    path('quan-ly-sach/add/', views.addBook, name = "addBook"),
    path('addBookPost/', views.addBookPost, name="addBookPost"),
    #sua sach
    path('quan-ly-sach/update/<str:id_sach>/', views.updateBook, name="updateBook"),
    path('updateBookPost/', views.updateBookPost, name="updateBookPost"),
    #xoa sach
    path('quan-ly-sach/delete/<str:id_sach>/', views.deleteBook, name="deleteBook"),
    #tim kiem sach
    path('quan-ly-sach/search/<str:searchInput>/', views.searchBook, name="searchBook"),
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    path('quan-ly-tinh-hinh-muon-tra/', views.quanlytinhhinhmuontra, name="quanlytinhhinhmuontra"),
    path('quan-ly-kho-sach/', views.quanlykhosach, name="quanlykhosach"),
    path('logout/', views.logout, name="logout"),
    # Form action submit
    path('loginPost/', views.loginPost, name='loginPost'),
]