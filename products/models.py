from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



class Product(models.Model):

    CATEGORY_CHOICES = [
        ('ebooks', 'eBooks'),
        ('software', 'Software'),
        ('music', 'Music'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    digital_file = models.FileField(upload_to='products_files/')
    image = models.ImageField(upload_to='product_images/')
    seller = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )  
    views = models.PositiveIntegerField(default=0)
    sold = models.PositiveIntegerField(default=0)

    
    def bought_by(self, user):
        return self.orders.filter(buyer=user).exists()



class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/',default="default_avatar.png", null=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.user.username
    

class Order(models.Model):

    product = models.ForeignKey(Product,related_name='orders',on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.buyer.username} - {self.product.name}"
    


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} - {self.product} review"