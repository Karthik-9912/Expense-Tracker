from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    form=RegistrationForm()
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            print("Successfull")
            # form.save()
    context={
        'form':form
    }
    return render(request,'register.html',context)


def log_in(request):

    return render(request,'login.html')