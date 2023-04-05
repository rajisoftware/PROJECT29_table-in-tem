from django.shortcuts import render

# Create your views here.
from app.models import *
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',d)
def display_Webpage(request):
    LOW=Webpage.objects.all()
    d={'topics':LOW}
    return render(request,'display_Webpage.html',d)
