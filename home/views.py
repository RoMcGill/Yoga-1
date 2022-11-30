from django.shortcuts import render


def index(request):
    return render(request, 'home/home.html', {})

def How(request):
    return render(request, 'home/how.html', {})