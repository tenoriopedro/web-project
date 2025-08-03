from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bancadas


def index(request):
    return render(
        request,
        'products/index.html'
    )


class BancadaListView(ListView):
    model = Bancadas
    template_name = 'products/bancadas.html'
    context_object_name = 'bancadas'


class BancadaDetailView(DetailView):
    model = Bancadas
    template_name = 'products/bancada_detail.html'
    context_object_name = 'bancada'