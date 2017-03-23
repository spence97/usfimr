from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    context = {}

    return render(request, 'usfimr/home.html', context)

def map(request):
    """
    Controller for map page.
    """

    context = {}

    return render(request, 'usfimr/map.html', context)

def info(request):
    """
    Controller for map page.
    """

    context = {}

    return render(request, 'usfimr/info.html', context)
