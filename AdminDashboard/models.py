from django.db import models
from users.models import CustomUser


# Create your models here.

#   #### Product Model ####
class productsModel(models.Model):
    Sari_Name = models.CharField(max_length=100)
    Description = models.TextField()
    Image = models.ImageField(upload_to='images/')
    Price = models.TextField()
    LDescription = models.TextField()
    Size = models.TextField()


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='product_images/')


class Order(models.Model):
    sari_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_images/')
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    number = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)