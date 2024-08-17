from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'RZD',
        'content': 'Главная страница',
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
