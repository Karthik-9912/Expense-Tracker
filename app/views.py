from django.shortcuts import render,redirect
from .models import Account,Income,Expense
from decimal import Decimal

# Create your views here.
def index(request):
    data=Account.objects.first()
    context={
        'data':data
    }
    return render(request,'index.html',context)

def chart(request):
    return render(request,'chart.html')

def budget(request):
    return render(request,'budget.html')


def transaction(request):
    data=Account.objects.first()
    if request.method=="POST":
        amt=request.POST.get('amt')
        exp=request.POST.get('exp')
        inc=request.POST.get('inc')
        date=request.POST.get('date')
        desc=request.POST.get('desc')
        if data and amt:
            amt=Decimal(amt)

            if inc:
                data.cash+=amt
                data.save()
                Income.objects.create(
                    income_type=inc,date=date,note=desc,amount=amt
                )
                data1.save()
            if exp:
                data.cash-=amt
                data.save()
                Expense.objects.create(
                    expense_type=exp,date=date,note=desc,amount=amt
                )
                data2.save()
    data1=Income.objects.all()
    data2=Expense.objects.all()
    context={
        'data':data,
        'data1':data1,
        'data2':data2,
    }
    return render(request,'transaction.html',context)

def delete_inc(request,d1):
    data=Income.objects.get(id=d1)
    data.delete()
    return redirect('transaction')
def delete_exp(request,d2):
    data=Expense.objects.get(id=d2)
    data.delete()
    return redirect('transaction')
