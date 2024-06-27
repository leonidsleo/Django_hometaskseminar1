from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:klient_id>/<int:days_order>', views.order, name='orders'),
    path('add_product/', views.add_product, name='add_product'),
]