from tkinter.font import names
from .import views
from django.urls import path
from .views import *


urlpatterns = [

    # login register logout

    path('register/', views.RegisterView.as_view(), name='user-register'),
    path('verify-otp/', OTPVerifyView.as_view(), name='verify-otp'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:pk>/',Userdetails.as_view(),name='user') ,
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password-reset/', views.PasswordResetView.as_view(), name='password-reset'),
    path('password-otp/', views.PassOTPVerificationView.as_view(), name='otp-verification'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),


#created book

    path('category/', Categoyycreateview.as_view(), name='category'),
    path('category/<int:pk>/', Categorydetails.as_view(), name='category_details'),
    path('book/', Bookcreateview.as_view(), name='book'),
    path('book/<int:pk>/', Bookdetails.as_view(), name='book_details'),
    path('customer/', CustomercreateView.as_view(), name='customer'),
    path('customer/<int:pk>/',Customerdetails.as_view(),name='customer_details'),
    path('order/',Ordercreateview.as_view(),name='order'),
    path('order/<int:pk>/',Orderdetails.as_view(),name='orderdetails'),
]