

from email.policy import default
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import Account

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from store .models import Product, category


def index(request):
    products=Product.objects.all().filter(is_available=True)
    categories=category.objects.all()
   
    Products=None
    context={
        'products':products,
        'categories':categories,
    }
    return render(request,'index.html',context)



def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method =='POST':
            email=request.POST.get('email')
            password=request.POST.get('password')
            user = authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                messages.info(request,"user name or password is invalid")

        context={}
        return render(request,'loginpage.html',context)



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            phone_number  = form.cleaned_data['phone_number']
            email  = form.cleaned_data['email']
            password  = form.cleaned_data['password']
            username=email.split("@")[0]
            user= Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username, password=password)
            user.phone_number=phone_number
            user.save()
            messages.success(request,'Registration successful')
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request,'register.html',context)


@login_required(login_url='loginpage')
def logoutUser(request):
    logout(request)
    return redirect('loginpage')


