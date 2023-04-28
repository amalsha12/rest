from django.shortcuts import render,redirect
from .models import Food
from .forms import Foodforms
def add(request):
    if request.method=="POST":
        foodday=request.POST.get('foodday',)
        foodname=request.POST.get('foodname',)
        foodimg=request.FILES['foodimg']
        fooddesc=request.POST.get('fooddesc',)
        add=Food(foodday=foodday,foodname=foodname,foodimg=foodimg,fooddesc=fooddesc)
        add.save()
        return redirect('/')

    return render(request,'add.html')
def detail(request,food_id):
    food=Food.objects.get(id=food_id)
    return render(request,'detail.html',{'food':food})
def indexop(request):
    food=Food.objects.all()
    context={'foodlist':food}
    # return render(request,'detail.html',context)
    return render(request,'indexop.html',context)


def update(request,food_id):
    food=Food.objects.get(id=food_id)
    form=Foodforms(request.POST or None, request.FILES,instance=food)
    if form.is_valid():
        form.save()
        return redirect('/')
    
    return render(request,'edit.html',{'form':form,'food':food})


def delete(request,food_id):
    if request.method=='POST':
        food=Food.objects.get(id=food_id)
        food.delete()
        return redirect('/')
    return render (request,'delete.html')
 

# Create your views here.
