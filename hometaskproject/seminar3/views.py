from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

import logging

from django.utils import timezone
from datetime import timedelta, datetime
from .models import Klient, Order, Product
from .forms import ProductForm



logger = logging.getLogger(__name__)


def index(request):
    context = {
        'title': 'Главная страница'
    }
    logger.info('Запущена стартовая страница')
    return render(request, 'seminar3/index.html', context)


def order(request, klient_id, days_order):
    products = []
    product_set=[]
    today = datetime.now()
    klient = Klient.objects.filter(pk=klient_id).first()
    orders = Order.objects.filter(order_klient=klient, date_order__gte=today-timedelta(days=days_order)).all()
    for order in orders:
        products = order.order_product.all()
        for product in products:
            if product not in product_set:
                product_set.append(product)
    
    context = {
            'title': f'Заказы клиента {klient.name}',
            'клиент': klient,
            'дни': days_order,
            'продукты': product_set,       
    }

    return render(request, 'seminar3/order.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name_product = form.cleaned_data['name_product']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            product = Product(name_product=name_product, description=description, price=price, quantity=quantity, image=image)
            product.save()
            message = 'Продукт добавлен'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'seminar3/add_product.html', {'form': form, 'message': message})