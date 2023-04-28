from django.shortcuts import render
from . models import Specials,Varieties
def indexf(request):
    object=Specials.objects.all()
    object1=Varieties.objects.all()
    return render(request,'index.html',{'result':object,'result1':object1})
    
# Create your views here.
