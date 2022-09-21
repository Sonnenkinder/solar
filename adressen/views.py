from cProfile import Profile
import datetime
from multiprocessing import context
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.http import HttpResponse
from django.template import loader

from .models import Adressen




# Create your views here.

class AdressHome(ListView):
    model = Adressen
    template_name = 'adressen/adress_home.html'

class AdressCreate(CreateView):
    model = Adressen
    template_name = 'adressen/adress_create.html'
    fields = '__all__'
    success_url = reverse_lazy('adress_start')

class AdressDetail(DetailView):
    model = Adressen
    template_name = 'adressen/adress_detail.html'

class AdressUpdate(UpdateView):
    model = Adressen
    template_name = 'adressen/adress_update.html'
    fields = '__all__'

class AdressDelete(DeleteView):
    model = Adressen
    template_name = 'adressen/adress_delete.html'
    success_url = reverse_lazy('adress_start')

class AdressLauf(DetailView):
    model = Adressen
    template_name = 'adressen/adress_lauf.html'
    fields = '__all__'

class AdressBer(DetailView):
    model = Adressen
    template_name = 'adressen/adress_ber.html'
    fields = '__all__'

class AdressKal(DetailView):
    model = Adressen
    template_name = 'adressen/adress_kal.html'

def index(request):
     template = loader.get_template('adressen/adress_lauf.html')
     context = {}
     return HttpResponse(template.render(context, request))



