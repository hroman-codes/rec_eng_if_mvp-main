from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.http import JsonResponse


def health(request):
    return JsonResponse({'status': 'ok'})


def index(request):
    return render(request, 'index.html')

def custom_404_view(request, exception):
    messages.error(request, '404 Not Found 🤦‍♂️')
    return render(request, 'errors/404.html', status=404)

# Serve React frontend
index = never_cache(TemplateView.as_view(template_name='index.html'))
