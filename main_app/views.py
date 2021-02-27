from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog

def home(request):
    return HttpResponse('<h1> Hello</h1>')

def about(request):
    return render(request, 'about.html')

def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', { 'dogs': dogs })