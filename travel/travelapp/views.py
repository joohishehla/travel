
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.

def demo(request):
    ob = Place.objects.all()
    ab = Team.objects.all()
    return render(request,'index.html',{'res':ob,'result':ab})


