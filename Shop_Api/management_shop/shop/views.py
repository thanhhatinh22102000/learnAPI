from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView
from django.http import JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import NhanVien_Serializer,KhachHang_Serializer,Product_Serializer
from .models import nhanvien,khachhang,product

# Create your views here.
class List_Create_Nhanvien(ListCreateAPIView):
    model=nhanvien
    serializer_class = NhanVien_Serializer

    def get_queryset(self):
        return nhanvien.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=NhanVien_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Create nhan vien successful!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Create nhan vien unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Nhanvien(RetrieveDestroyAPIView):
    model=nhanvien
    serializer_class = NhanVien_Serializer

    def put(self,request,*args,**kwargs):
        nv=get_object_or_404(nhanvien,id=kwargs.get('pk'))
        serializer=NhanVien_Serializer(nv,request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'message':'Update nhan vien successful!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Update nhan vien unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        nv=get_object_or_404(nhanvien,id=kwargs.get('pk'))
        nv.delete()

        return JsonResponse({'message':'Delete nhan vien successful'},status=status.HTTP_200_OK)




class List_Create_Khachhang(ListCreateAPIView):
    model=khachhang
    serializer_class = KhachHang_Serializer

    def get_queryset(self):
        return khachhang.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=KhachHang_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Create khach hang successful!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Create khach hang unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Khachhang(RetrieveDestroyAPIView):
    model=khachhang
    serializer_class = KhachHang_Serializer

    def put(self,request,*args,**kwargs):
        kh=get_object_or_404(khachhang,id=kwargs.get('pk'))
        serializer=KhachHang_Serializer(kh,request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'message':'Update  successfkhach hangul!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Update khach hang unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        kh=get_object_or_404(khachhang,id=kwargs.get('pk'))
        kh.delete()

        return JsonResponse({'message':'Delete khach hang successful'},status=status.HTTP_200_OK)





class List_Create_Product(ListCreateAPIView):
    model=product
    serializer_class = Product_Serializer

    def get_queryset(self):
        return product.objects.all()

    def create(self, request, *args, **kwargs):
        serializer=Product_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'Create product successful!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Create product unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

class Update_Delete_Product(RetrieveDestroyAPIView):
    model=product
    serializer_class = Product_Serializer

    def put(self,request,*args,**kwargs):
        pro=get_object_or_404(product,id=kwargs.get('pk'))
        serializer=Product_Serializer(pro,request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({'message':'Update product successful!'},status=status.HTTP_201_CREATED)
        return JsonResponse({'message':'Update product unsuccessful!'},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pro=get_object_or_404(product,id=kwargs.get('pk'))
        pro.delete()

        return JsonResponse({'message':'Delete product successful'},status=status.HTTP_200_OK)