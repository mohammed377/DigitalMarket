from django.contrib import admin

from .models import Product, UserProfile, Order,Review

    

admin.site.register(Product)
admin.site.register(UserProfile)  
admin.site.register(Order)
admin.site.register(Review)