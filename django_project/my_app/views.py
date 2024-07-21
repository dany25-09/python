from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<main><h1>hola<h1></main>")

def about(request):
    return HttpResponse("<h1>Sapo<h1>")