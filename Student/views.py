from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CreateUserForm,StudentForm
from django.contrib.auth import login, authenticate,logout
from .models import Student
# Create your views here.


def Login(request):
    context={}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"Username or password is incorrect")
    context={}
    return render(request,"Student/Login.html", context)

def Register(request):
    form = CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('Login')
    context = {'form':form}
    return render(request,"Student/Register.html", context)



def home(request):
    form = StudentForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        data=form.save(commit=False)
        form.instance.user = request.user
        form.save()

    context={"form":form}

    return render(request,"Student/setting.html",context)

def logout(request):
    logout(request)
    return redirect('Login')
