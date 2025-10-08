from django.shortcuts import render,redirect,get_object_or_404
from .models import Account,Income,Expense
from decimal import Decimal
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.
def index(request):
    data=Account.objects.first()
    if not data:
        Account.objects.create(cash=0.00)
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
    msg=""
    if not data:
        data=Account.objects.create(cash=0.00)
    if request.method=="POST":
        amt=request.POST.get('amt')
        category=request.POST.get('category')
        date=request.POST.get('date')
        desc=request.POST.get('desc')
        
        if data and amt:
            amt=Decimal(amt)
            if category=="income":
                data.cash+=amt
                data.save()
                Income.objects.create(
                    income_type=category,date=date,note=desc,amount=amt
                )
                
            elif category=="expense":
                data.cash-=amt
                data.save()
                Expense.objects.create(
                    expense_type=category,date=date,note=desc,amount=amt
                )
            else:
                msg="Please Select Category"
    data1=Income.objects.all()
    data2=Expense.objects.all()
    context={
        'data':data,
        'data1':data1,
        'data2':data2,
        'msg':msg,
    }
    return render(request,'transaction.html',context)

@require_POST
def delete_inc(request,d1):
    item=get_object_or_404(Income,id=d1)
    data=Account.objects.first()
    if data:
        data.cash-=Decimal(item.amount)
        data.save()
    item.delete()
    return redirect('transaction')

@require_POST
def delete_exp(request,d2):
    item=get_object_or_404(Expense,id=d2)
    data=Account.objects.first()
    if data:
        data.cash+=Decimal(item.amount)
        data.save()
    item.delete()
    return redirect('transaction')

