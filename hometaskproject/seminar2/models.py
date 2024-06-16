from django.db import models


class Klient(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=100)
    data_reg = models.DateField(auto_now_add=True)


class Product(models.Model):
    name_product = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    data_add = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    order_klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    order_product = models.ManyToManyField(Product)
    price_summ = models.DecimalField(decimal_places=2, max_digits=10)
    date_order = models.DateTimeField(auto_now_add=True)