from django import forms 
from .models import UserProfile,Product
from .models import Review

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'birth_date', 'avatar')




class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name','description','price','digital_file','image','category')

from django import forms    
from .models import Order      

class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order     
        fields = ('product', 'buyer')


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Review
        fields = ['rating', 'content']