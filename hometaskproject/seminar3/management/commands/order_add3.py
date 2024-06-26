from django.core.management.base import BaseCommand
from ...models import Order, Product, Klient


class Command(BaseCommand):
    help = "Добавить заказ"


    def add_arguments(self, parser):
        parser.add_argument('klient_pk', type=int, help='ID klient')
        parser.add_argument('produck_pk', type=int, help='ID product')
    

    def handle(self, *args, **kwargs):
        klient_pk = kwargs['klient_pk']
        produck_pk = kwargs['produck_pk']

        klient = Klient.objects.get(id=klient_pk)
        product = Product.objects.get(id=produck_pk)

        order = Order(order_klient=klient, order_summ = product.price * product.quantity)
        order.save()
        order.order_product.set([product])
        self.stdout.write(f'{order}')