from typing import Any
from django.core.management.base import BaseCommand, CommandParser
import seminar2.models as s2


class Command(BaseCommand):
    help = "Добавление пользователя"


    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Введите имя (add name)")
        parser.add_argument('email', type=str, help="Введите эл. почту (add email)")
        parser.add_argument('phone', type=str, help="Введите телефон (enter phone)")
        parser.add_argument('address', type=str, help="Введите ваш адрес (enter your address)")
        
    

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone = kwargs.get('phone')
        address = kwargs.get('address')
        klient = s2.Klient(name=name, email=email, phone=phone, address=address)
        klient.save()
        self.stdout.write(f'{klient}')