from multiprocessing import context
from django.shortcuts import render

def index(request):
    return render (request, "website/index.html")
# Create your views here.
def about(request):
    return render (request, "website/about.html")