from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, Order
# Create your views here.
def item_list(request):
    context = {'items':Item.objects.all()}
    return render(request,'item_list.html',context)
    #return HttpResponse('aaaaa')

def order_list(request):
    context ={'orders':Order.objects.all()}
    return render(request,'order_list.html',context)

def home(request):
    context = {'items': Item.objects.all()}
    return render(request,'home-page.html',context)

def checkout(request):
    return render(request,'checkout-page.html')

def product(request):
    return render(request,'product-page.html')