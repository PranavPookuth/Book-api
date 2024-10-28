from tkinter.font import names

from django.urls import path
from .views import *


urlpatterns = [
    path('category/', Categoyycreateview.as_view(), name='category'),
    path('category/<int:pk>/', Categorydetails.as_view(), name='category_details'),
    path('book/', Bookcreateview.as_view(), name='book'),
    path('book/<int:pk>/', Bookdetails.as_view(), name='book_details'),
    path('customer/', CustomercreateView.as_view(), name='customer'),
    path('customer/<int:pk>/',Customerdetails.as_view(),name='customer_details'),
    path('order/',Ordercreateview.as_view(),name='order'),
    path('order/<int:pk>/',Orderdetails.as_view(),name='orderdetails')
]