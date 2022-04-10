from django.shortcuts import render,HttpResponse,redirect
from .forms import takelist
from .forms import usercreation
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Todolist
import datetime
def home(request):
    return render(request,'test.html')
def createtodo(request):
    form = takelist()
    if request.method=="POST":
        form = takelist(request.POST)
        if form.is_valid():
            form.save()
           
            return HttpResponse('sucess')

    context={'form':form}        
    return render(request,'home.html',context)        

 
def signup(request):
    form = usercreation()
    if request.method=="POST":
        form = usercreation(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for' + user)
            return redirect('loginpage')
    context={'form':form}       
    return render(request,'register.html',context) 


def loginpage(request):
    if request.method=="POST":
        username = request.POST.get('username')    
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('authenticateduser')

    return render(request,'login.html')        
@login_required(login_url="loginpage")           
def authenticateduser(request):
    return render(request,'home2.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')
def viewtodo(request):
    print(datetime.date.today())
   
   
    result = Todolist.objects.filter(Remainder=datetime.date.today())
    print(result)
    context={'result':result}
    return render(request,'result.html',context)
