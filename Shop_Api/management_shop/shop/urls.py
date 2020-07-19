from django.urls import path
from .views import List_Create_Nhanvien,Update_Delete_Nhanvien,List_Create_Khachhang,Update_Delete_Khachhang,List_Create_Product,Update_Delete_Product
urlpatterns = [
    path('nhanvien/',List_Create_Nhanvien.as_view(),name='list_create_nv'),
    path('nhanvien/<int:pk>',Update_Delete_Nhanvien.as_view(),name='update_delete_nv'),
    path('khachhang/',List_Create_Khachhang.as_view(),name='list_create_kh'),
    path('khachhang/<int:pk>',Update_Delete_Khachhang.as_view(),name='update_delete_kh'),
    path('product/',List_Create_Product.as_view(),name='list_create_pro'),
    path('product/<int:pk>',Update_Delete_Product.as_view(),name='update_delete_pro'),
]