from django.shortcuts import render
from django.http import HttpResponse

import logging


logger = logging.getLogger(__name__)


def index(request):
    main = """
        <h1>Главная страница</h1>
        <p>Общая информация</p>
    """
    logger.info('Start page name')
    return HttpResponse(main)


def about(request):
    about_me = """
        <h1>Страница обо мне</h1>
        <p>Все обо мне</p>
    """
    logger.debug('Start page about')
    return HttpResponse(about_me)


# Create your views here.