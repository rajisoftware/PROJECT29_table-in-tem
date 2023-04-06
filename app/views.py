from django.shortcuts import render
from django.db.models.functions import Length

# Create your views here.
from app.models import *
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',d)
def display_Webpage(request):
    LOW=Webpage.objects.all() 
    LOW=Webpage.objects.filter(name='raj')
    #LOW=Webpage.objects.get(name='virat')
    LOW=Webpage.objects.exclude(name='raj')
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.all().order_by('name')
    LOW=Webpage.objects.all().order_by('-name')
    LOW=Webpage.objects.all().order_by(Length('name'))
    LOW=Webpage.objects.all().order_by(Length('name').desc())
    d={'webpages':LOW}
    return render(request,'display_Webpage.html',d)
def Access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='1998-10-23')
    LOA=AccessRecord.objects.filter(date__gte='1998-10-23')
    LOA=AccessRecord.objects.filter(date__lt='2000-11-23')
    LOA=AccessRecord.objects.filter(date__lte='2000-11-23')
    d={'access':LOA}
    return render(request,'Access.html',d)
