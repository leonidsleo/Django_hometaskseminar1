from django.core.management.base import BaseCommand, CommandParser
from ...models import Product


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