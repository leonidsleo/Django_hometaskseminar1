from django.core.management.base import BaseCommand, CommandParser
from seminar2.models import Product


class Command(BaseCommand):
    help = "Добавление продуктов"


    def add_arguments(self, parser):
        parser.add_argument('name_product', type=str, help="Введите наименование продукта (ender product)")
        parser.add_argument('description', type=str, help="Описание продукта")
        parser.add_argument('price', type=float, help="Стоимость товара")
        parser.add_argument('quantity', type=float, help="Количество товара")
        

    def handle(self, *args, **kwargs):
        name = kwargs.get('name_product')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        product = Product(name_product=name, description=description, price=price, quantity=quantity)
        product.save()
        self.stdout.write(f'{product}')

        """
from django.core.management.base import BaseCommand
from django.utils import timezone
from store.storeapp.models import OrderModel
from store.storeapp.models import ClientModel
from store.storeapp.models import ProductModel
from random import choice


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        order = OrderModel(
            client=choice(ClientModel.objects.all()),
            total_price=0,
        )
        order.save()
        for _ in range(10):
            product = choice(ProductModel.objects.all())
            order.products.add(product)
            order.total_price += product.price

        print('Add new order')
"""

"""
class ClientModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=40)
    registration = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone:{self.phone}, adress: {self.adress}'


class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quanty = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    #image = models.ImageField(upload_to=upload_image)


class OrderModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductModel)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
"""