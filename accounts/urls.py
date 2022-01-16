from django.urls import path
from . import views



urlpatterns = [
    path('api/users/', views.UserCreate.as_view(), name='account-create'),

    path('sellers/', views.SellerList.as_view(), name='seller-create'),
    path('sellers/<int:pk>/', views.SellerDetail.as_view(), name='seller-detail'),

    path('products/', views.ProductList.as_view(), name='product-create'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='Product-detail'),
        
]

