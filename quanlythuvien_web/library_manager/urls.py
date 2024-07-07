from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('home/', views.home, name="home"),
    # Url quan ly nguoi dung / user
    path('quan-ly-nguoi-dung/<str:tab>/', views.quanlynguoidung, name="quanlynguoidung"),
    # Add user
    path('quan-ly-nguoi-dung/nguoi-dung/add/', views.addUser, name="addUser"),
    path('addUserPost/', views.addUserPost, name="addUserPost"),
    # Update user
    path('quan-ly-nguoi-dung/nguoi-dung/update/<str:id>/', views.updateUser, name="updateUser"),
    path('updateUserPost/', views.updateUserPost, name="updateUserPost"),
    # Delete user
    path('quan-ly-nguoi-dung/nguoi-dung/delete/<str:id>/', views.deleteUser, name="deleteUser"),
    # Search user
    path('quan-ly-nguoi-dung/nguoi-dung/search/<str:searchInput>/', views.searchUser, name="searchUser"),

    # Url quan ly nguoi dung / Add doc-gia post
    path('quan-ly-nguoi-dung/doc-gia/add/', views.addDocgia, name="addDocgia"),
    path('addDocgiaPost/', views.addDocgiaPost, name="addDocgiaPost"),
    # Update doc-gia
    path('quan-ly-nguoi-dung/doc-gia/update/<str:id>/', views.updateDocgia, name="updateDocgia"),
    path('updateDocgiaPost/', views.updateDocgiaPost, name="updateDocgiaPost"),
    # Delete doc-gia
    path('quan-ly-nguoi-dung/doc-gia/delete/<str:id>/', views.deleteDocgia, name="deleteDocgia"),
    # Search doc-gia
    path('quan-ly-nguoi-dung/doc-gia/search/<str:searchInput>/', views.searchDocgia, name="searchDocgia"),

    # Quan ly danh muc
    path('quan-ly-danh-muc/', views.quanlydanhmuc, name="quanlydanhmuc"),
    # add category
    path('quan-ly-danh-muc/add/', views.addUsertoCategory, name="addUsertoCategory"),
    path('addCategoryPost/', views.addCategoryPost, name="addCategoryPost"),
    #update category
    path('quan-ly-danh-muc/update/<str:id>/', views.updateCategory, name="updateCategory"),
    path('updateCategoryPost/', views.updateCategoryPost, name="updateCategoryPost"),
    path('quan-ly-danh-muc/search/<str:searchInput>/', views.searchCategories, name="searchCategory"),
    #delete category
    path('quan-ly-danh-muc/delete/<str:id>/', views.deleteCategory, name="deleteCategory"),
    #url quan ly sach
    path('quan-ly-sach/', views.quanlysach, name="quanlysach"),
    path('home/quanlysach/index.html', views.quanlysach, name='quanlysach'),
    #add sach
    path('quan-ly-sach/add/', views.addBook, name = "addBook"),
    path('addBookPost/', views.addBookPost, name="addBookPost"),
    #sua sach
    path('quan-ly-sach/update/<str:id_sach>/', views.updateBook, name="updateBook"),
    path('updateBookPost/', views.updateBookPost, name="updateBookPost"),
    #xoa sach
    path('quan-ly-sach/delete/<str:id_sach>/', views.deleteBook, name="deleteBook"),
    #tim kiem sach
    path('quan-ly-sach/search/<str:searchInput>/', views.searchBook, name="searchBook"),
    #hien thi home

    # Quản lý mượn trả sách
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    # Get books from javascript fetch request - phieumuon
    path('getBooks_Phieumuon/', views.getBooks_phieumuon, name="getBooksPhieumuon"),
    # Get info pheumuon by id from fetch request js
    path('get_info_phieumuonById/<str:id>/', views.get_info_phieumuonById, name="getInfoPhieumuonById"),
    # Get info thethuvien from fetch request js
    path('get_info_thethuvienById/', views.get_info_thethuvienById, name="getInfoThethuvienById"),
    # Add phieumuon from fetch js
    path('addPhieumuonPost/', views.addPhieumuonPost, name="addPhieumuonPost"),
    # Update phieumuon from fetch js
    path('updatePhieumuonPost/', views.updatePhieumuonPost, name="updatePhieumuonPost"),
    # Delete phieumuon
    path('quan-ly-muon-tra/delete/<str:id>/', views.deletePhieumuon, name="deletePhieumuon"),
    # Search phieumuon by id_the fetch js
    path('quan-ly-muon-tra/search-by-idThe/<str:id_the>/', views.searchPhieumuonByIdThe, name="searchPhieumuonByIdThe"),
    # Tra sach phieumuon fetch js
    path('quan-ly-muon-tra/trasach/', views.trasach, name="trasach"),

    #quan ly tinh hinh muon tra
    path('quan-ly-tinh-hinh-muon-tra/', views.quanlytinhhinhmuontra, name="quanlytinhhinhmuontra"),
    
    # Quan ly kho sach
    # Get book by id from javascript fetch request
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
    # Quan ly kho sach - huy sach
    path("quan-ly-kho-sach/huy-sach/", views.huysach, name="huysachIndex"),
    # Quan ly kho sach - huy sach - add view
    path("quan-ly-kho-sach/huy-sach/add/", views.addPhieuhuy, name="addPhieuhuy"),
    # Post request add huy sach
    path('huysachPost/', views.huysachPost, name="huysachPost"),
    # Quan ly kho sach - huy sach - update view
    path("quan-ly-kho-sach/huy-sach/update/<str:id>/", views.updatePhieuhuy, name="updatePhieuhuy"),
    # Post request update phieuhuy sach
    path('updatePhieuhuyPost/', views.updatePhieuhuyPost, name="updatePhieuhuyPost"),
    # Delete phieuhuy
    path("quan-ly-kho-sach/huy-sach/delete/<str:id>/", views.deletePhieuhuy, name="deletePhieuhuy"),
    # Info phieuhuy
    path("quan-ly-kho-sach/huy-sach/info/<str:id>/", views.infoPhieuhuy, name="infoPhieuhuy"),
    # Search phieu nhap by date
    path('quan-ly-kho-sach/huy-sach/search/<str:dateFrom>/<str:dateTo>/', views.searchPhieuhuyByDate, name="searchPhieuhuyByDate"),

    path('quan-ly-tinh-hinh-muon-tra/load-form', views.quanlytinhhinhDaTra, name="quanlytinhhinhDaTra"),

    path('logout/', views.logout, name="logout"),
    # Form action submit
    path('loginPost/', views.loginPost, name='loginPost'),
    path('register/', views.register, name="register"),
    path('registerPost/', views.registerPost, name='registerPost'),

    # ket Quan ly sach ton kho
    path('thong-ke/ton-kho/search/<str:searchInput>/', views.searchThongKeSachTK ,name="searchThongKeSachTK"),
    #thong ke
    path('thong-ke/nhap-huy/', views.ThongKeNhapHuy, name="ThongKeNhapHuy" ),
    path('thong-ke/ton-kho/', views.ThongKeTongKho, name="ThongKeTongKho"),
]