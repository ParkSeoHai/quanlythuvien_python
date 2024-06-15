from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('home/', views.home, name="home"),
    path('quan-tri-he-thong/', views.quantrihethong, name="quantrihethong"),
    path('quan-ly-kho-sach/', views.quanlykhosach, name="quanlykhosach"),
    path('quan-ly-doc-gia/', views.quanlydocgia, name="quanlydocgia"),
    path('quan-ly-muon-tra/', views.quanlymuontra, name="quanlymuontra"),
    path('bao-cao-thong-ke/', views.baocaothongke, name="baocaothongke")
]