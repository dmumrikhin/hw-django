from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import path
from . import views

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    phones = []
    for row in phone_objects:
        print(row)
        phones.append(row)
    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.filter(slug=slug)[0]
    template = 'product.html'
    context = {
        'phone': phone_object,
    }
    return render(request, template, context)

