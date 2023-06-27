from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm  
from .models import Product,Order ,UserProfile,Review
from .forms import ProductForm,OrderForm,UserProfileForm,ReviewForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.http import HttpResponse,HttpResponseBadRequest,HttpResponseNotFound
from django.shortcuts import get_object_or_404,redirect
from django.utils.encoding import smart_str


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    
class UserCreateView(CreateView): 
    form_class = UserCreationForm   
    template_name = 'accounts/register.html'   
    success_url = '/login/'    



class LogoutView(RedirectView):  
    url = '/login/'
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
class UserProfileUpdateView(UpdateView):     
    form_class = UserProfileForm        
    template_name = 'accounts/profile_update_form.html'       
    success_url = '/profile/'           
    def get_object(self):         
        if self.request.user.is_authenticated:          
            return self.request.user.user_profile

class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'accounts/profile.html'
    
    def get_object(self):
        return self.request.user.user_profile
from django.urls import reverse
   

class ProductCreateView(LoginRequiredMixin,CreateView):     
    model = Product     
    form_class = ProductForm     
    template_name = 'products/product_create.html'
    login_url = '/login/'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.seller = self.request.user
        self.object.save()
        return super().form_valid(form)     
    def get_success_url(self):
       return reverse('product_list')
    
    
class ProductUpdateView(LoginRequiredMixin,UpdateView):  
    login_url = '/login/' 
    model = Product   
    form_class = ProductForm       
    template_name = 'products/product_update.html'

class ProductListView(ListView):    
    model = Product    
    template_name = 'products/product_list.html'

class ProductDetailView(DetailView):   
    model = Product   
    template_name = 'products/product_detail.html'
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['bought'] = self.object.bought_by(self.request.user.id)
       return context
    


class CreateOrderView(LoginRequiredMixin,DetailView):
    model = Product
    template_name = 'orders/create_order.html'
    login_url = '/login/'
    
    def post(self, request, *args, **kwargs):
        product = self.get_object()
        user_profile = UserProfile.objects.get(user=request.user.id)
        
        if user_profile.balance >= product.price:
            # Create order
            Order.objects.create(
                product=product,
                buyer=request.user,
            )
            
            # Update user balance     
            user_profile.balance -= product.price      
            user_profile.save()
            
            # Increment product sold           
            product.sold +=1          
            product.save()
            
            return self.download_file(product)
    
    def download_file(self, product):
       file_path = product.digital_file.path   
       with open(file_path, 'rb') as f:
         response = HttpResponse(f.read(), content_type='application/force-download')
         response['Content-Disposition'] = 'attachment; filename=' + product.digital_file.name
         return response
    
class OrderListView(LoginRequiredMixin,ListView):      
    model = Order               
    template_name = 'order_list.html'


from django.core.exceptions import PermissionDenied


def download_file(request,product_id):
    product=Product.objects.get(id=product_id)
    if not Order.objects.filter(
            product_id=product.id,           
            buyer_id=request.user.id
         ).exists():  
             raise PermissionDenied
              
    file_path = product.digital_file.path   
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename=' + product.digital_file.name
        return response
    


class CreateReview(CreateView):
    model = Review
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product_id = self.kwargs['product_id']
        return super().form_valid(form)