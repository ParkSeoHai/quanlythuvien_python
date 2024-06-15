from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def quantrihethong(request):
    template = loader.get_template('quantrihethong.html')
    return HttpResponse(template.render())

def quanlykhosach(request):
    template = loader.get_template('quanlykhosach.html')
    return HttpResponse(template.render())

def quanlydocgia(request):
    template = loader.get_template('quanlydocgia.html')
    return HttpResponse(template.render())

def quanlymuontra(request):
    template = loader.get_template('quanlymuontra.html')
    return HttpResponse(template.render())

def baocaothongke(request):
    template = loader.get_template('baocaothongke.html')
    return HttpResponse(template.render())