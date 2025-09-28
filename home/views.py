from django.shortcuts import render , redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    msg=''
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            msg="Success!!"
            form.save()
            
    context={
        'form':form,
        'msg':msg
    }
    return render(request,"register.html",context)

def log_in(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        # print(username,password)
        try:
            a = User.objects.get(username = username)
            print(a)
        except:
            msg="User not found! Register.."
        user = authenticate(request,username=username , password=password)
        print(user)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            msg = "Password is incorrect!!"            
    context={
            'msg':msg
        }
    return render(request,'login.html',context)