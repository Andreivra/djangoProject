from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required()
def show_name(request):
    return HttpResponse('Hello world')


@login_required()
def show_another_name(request):
    return HttpResponse('Hello world no 2')


@login_required()
def cars(request):
    list_of_cars = {
        'all_cars': [
            {
                'brand': 'Audi',
                'model': 'A6',
                'year': 2003
            }, {
                'brand': 'Ford',
                'model': 'Ranger',
                'year': 2022
            }, {
                'brand': 'Dacia',
                'model': 'Spring',
                'year': 2021
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', list_of_cars)


@login_required()
def books(request):
    list_of_books = {
        'all_books': [
            {
                'autor': 'Mario Puzzo',
                'titlu': 'Arena sumbra',
                'an': 1936,
                'gen': 'Drama'
            }, {
                'autor': 'Mihai Eminescu',
                'titlu': 'Luceafarul',
                'an': 1925,
                'gen': 'Poezie'
            }, {
                'autor': 'Mario Puzzo',
                'titlu': 'Arena sumbra',
                'an': 1936,
                'gen': 'Drama'
            }, {
                'autor': 'Mario Puzzo',
                'titlu': 'Arena sumbra',
                'an': 1936,
                'gen': 'Drama'
            }
        ]
    }

    return render(request, 'intro/list_of_books.html', list_of_books)
