from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import os, csv

BUS_STATION_CSV = settings.BUS_STATION_CSV
with open(BUS_STATION_CSV, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    CONTENT = []
    for row in reader:
        CONTENT.append(row)

def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(CONTENT, 10)
    bus_stations = paginator.get_page(page_number)
    context = {
        # 'bus_stations': bus_stations,
        'page_number': page_number,
        'page': bus_stations,
    }
    return render(request, 'stations/index.html', context)
