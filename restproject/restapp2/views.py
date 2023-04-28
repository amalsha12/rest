from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
def register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
        user.save()
        print("user created")
        messages.success(request,'registration successfully done! ')
        return redirect('login')
    return render(request,'register.html')
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            error="invalid user"
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
