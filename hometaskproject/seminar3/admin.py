from django.contrib import admin
from .models import Product, Klient, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'price', 'quantity', 'data_add']
    ordering = ['name_product', 'price']
    list_filter = ['name_product', 'quantity', 'data_add']
    search_fields = ['name']
    search_help_text = 'Поиск по наименованию (name)'
    readonly_fields = ['data_add']
    fieldsets = [
        (
            "Товар",
            {
                'classes': ['wide'],
                'fields': ['name_product', 'image'],
            },
        ),
        (
            "Описание товара",
            {
                'classes': ['collapse'],
                'description': 'Здесь подроное описание товара',
                'fields': ['description'],
            },
        ),
        (
            "Наличие, цена",
            {
                'fields': ['price', 'quantity'],
            },
        ),
    ]


class KlienAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    ordering = ['name', 'email', 'phone', 'address']
    list_filter = ['name', 'address']
    search_fields = ['name', 'phone']
    search_help_text = 'Поиск по имени и телефону (name, phone)' 


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_summ', 'date_order']
    # 'order_klient', 'order_product', 
    ordering = ['order_summ', '-date_order']
    list_filter = ['order_klient', 'order_product', 'date_order']
    search_fields = ['order_klient']
    search_help_text = 'Поиск по клиенту (order_klient)'


admin.site.register(Product, ProductAdmin)
admin.site.register(Klient, KlienAdmin)
admin.site.register(Order, OrderAdmin)
