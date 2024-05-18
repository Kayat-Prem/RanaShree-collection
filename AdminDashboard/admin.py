from django.contrib import admin
from .models import productsModel
<<<<<<< HEAD
from .models import Cart, Order

=======
from .models import Cart
from .models import Order
>>>>>>> origin/main

# Register your models here.
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'Sari_Name', 'Description', 'display_image', 'Price')

    def display_image(self, obj):
        return '<img src="{}" width="100" />'.format(obj.Image.url)

    display_image.allow_tags = True
    display_image.short_description = 'Image'

# Register the productsModel class with the custom admin class
admin.site.register(productsModel, ProductsModelAdmin)


class CartModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_name', 'description', 'price', 'size', 'quantity', 'image',)

admin.site.register(Cart, CartModelAdmin)

class OrderAdmin(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'sari_name', 'quantity', 'total_price', 'size', 'image', 'full_name', 'address', 'number', 'user')
=======
    list_display = ('id', 'sari_name', 'price', 'size', 'image', 'full_name', 'address', 'number', )
>>>>>>> origin/main
    
admin.site.register(Order, OrderAdmin)






<<<<<<< HEAD
=======


>>>>>>> origin/main
