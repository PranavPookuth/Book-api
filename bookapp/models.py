from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    C_name=models.CharField(max_length=200)
    def __str__(self):
        return self.C_name

class Book(models.Model):
    category=models.ForeignKey(Category,related_name='bookname',on_delete=models.CASCADE)
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    published_date=models.DateField()
    summary=models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.book_name

class Customer(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer,self.book


