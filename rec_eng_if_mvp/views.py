from django.shortcuts import render
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def custom_404_view(request, exception):
    messages.error(request, '404 Not Found 🤦‍♂️')
    return render(request, 'errors/404.html', status=404)
