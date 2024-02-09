from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.conf import settings
import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open(settings.BUS_STATION_CSV, encoding='utf-8') as file:
    reader = csv.DictReader(file)
    all_stations = []
    for element in reader:
        all_stations.append({'Name': element['Name'], 'Street': element['Street'], 'District': element['District']})


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(all_stations, 5)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page_number,
    }
    return render(request, 'stations/index.html', context)
