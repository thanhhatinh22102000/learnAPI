from django.db import models

# Create your models here.
class nhanvien(models.Model):
    id_nv=models.CharField(max_length=100)
    name_nv=models.CharField(max_length=255)
    age_nv=models.IntegerField()
    address_nv=models.CharField(max_length=255)

    def __str__(self):
        return self.name_nv

class khachhang(models.Model):
    id_kh=models.ForeignKey(nhanvien,on_delete=models.CASCADE)
    name_kh=models.CharField(max_length=255)
    address_kh=models.CharField(max_length=255)
    phone_kh=models.CharField(max_length=100)

    def __str__(self):
        return self.name_kh

class product(models.Model):
    id_pro=models.ForeignKey(khachhang,on_delete=models.CASCADE)
    name_pro=models.CharField(max_length=255)
    price_pro=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.name_pro