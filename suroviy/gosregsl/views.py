from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
from gosregsl.forms import AddRequest
from .forms import *
from .models import *
from django.views.generic.list import ListView
def index(request): #HttpResponse
    if request.method == 'POST':
        form = AddRequest(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('requests')
    else:
        form = AddRequest()
    return render(request, 'suroviy/index.html', {'form': form, 'title': 'Главная страница'})

class RequestView(ListView):
    template_name = 'suroviy/request.html'
    model = Baza
    context_object_name = 'Baza'

def sotrudnic(request): #HttpResponse
    return redirect('sotrudnic')
def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
