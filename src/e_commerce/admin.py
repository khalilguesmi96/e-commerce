from django.contrib import admin
from .models import Item, OrderItem, Order
# Register your models here.
class AdminItem(admin.ModelAdmin):
        list_display = ('title', 'price', 'image', 'category', 'label')
        list_display_links = ['title']
        search_fields = ['title', 'price', 'category']
        list_filter = ['category', 'label']


class AdminOrder(admin.ModelAdmin):
    list_display = ('use', 'start_date', 'ordered_date', 'ordered')
    list_display_links = ['use']
    search_fields = ['use', 'items', 'ordered']
    list_filter = ['start_date', 'ordered_date']


admin.site.register(Item,AdminItem)
admin.site.register(OrderItem)
admin.site.register(Order,AdminOrder)
