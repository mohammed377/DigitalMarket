from django.urls import path
from .views import (
    UserLoginView,
    UserCreateView,    
    UserProfileUpdateView,
    ProductCreateView, 
    ProductUpdateView,
    ProductListView,
    ProductDetailView,
    CreateOrderView,
    OrderListView,
    UserProfileView,
    LogoutView,
    download_file,
    CreateReview
)

urlpatterns = [    
    path('', ProductListView.as_view(), name='product_list'),  
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/', UserProfileUpdateView.as_view(), name='profile_update'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),     
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('product/<int:pk>/order/', CreateOrderView.as_view(), name='create_order'),
path('products/<int:product_id>/download/', download_file, name='product-file-download'),
path('<int:product_id>/review/', CreateReview.as_view(), name='create_review'),
]