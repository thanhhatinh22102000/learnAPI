from rest_framework import serializers
from .models import khachhang,nhanvien,product

class NhanVien_Serializer(serializers.ModelSerializer):
    class Meta:
        model=nhanvien
        fields='__all__'

class KhachHang_Serializer(serializers.ModelSerializer):
    class Meta:
        model=khachhang
        fields='__all__'

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'