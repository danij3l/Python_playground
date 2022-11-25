from django.shortcuts import render
from .models import *

def home(request):
    animals = Animals.objects.all()
    return render(request,'home.html', {'animals':animals})

def about(request):
    return render(request,'about.html')