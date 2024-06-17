"""
URL configuration for ShopSphere project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from shop import views
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/v1/register/", views.SignUpView.as_view()),
    path("api/v1/token/", ObtainAuthToken.as_view()),
    path("api/v1/products/", views.ProductListView.as_view()),
    path("api/v1/products/<int:pk>/", views.ProductDetailView.as_view()),
    path("api/v1/products/<int:pk>/addtocart/", views.AddToCartView.as_view()),
    path("api/v1/carts/", views.CartListView.as_view()),
    path("api/v1/carts/<int:pk>/", views.CartItemUpdateView.as_view()),
    path("api/v1/order/", views.CheckOutView.as_view()),
    path("api/v1/order/summary/", views.OrderSummaryView.as_view()),
    path("api/v1/payment/verification/", views.PaymentVerificationView.as_view()),
    
]
