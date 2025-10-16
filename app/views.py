from django.shortcuts import render,redirect,get_object_or_404
from .models import Account,Income,Expense
from decimal import Decimal
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Sum

# Create your views here.
def index(request):
    data=Account.objects.first()
    if not data:
        Account.objects.create(cash=0.00)
    context={
        'data':data
    }
    return render(request,'index.html',context)



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

    if not data1.exists():
        tot_income=0.00
    else:
        tot_income=sum(i.amount for i in data1)

    if not data2.exists():
        tot_expense=0.00
    else:
        tot_expense=sum(e.amount for e in data2)

    context={
        'data':data,
        'data1':data1,
        'data2':data2,
        'tot_income':tot_income,
        'tot_expense':tot_expense,
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


def chart(request):
    return render(request,'chart.html')

def chart_data(request):
    expenses=Expense.objects.values('expense_type').annotate(total=Sum('amount'))
    incomes=Income.objects.values('income_type').annotate(total=Sum('amount'))

    expense_data={
        "labels":[e['expense_type']for e in expenses],
        "data":[float(e['total'])for e in expenses]
    }

    income_data={
        "labels":[i['income_type']for i in incomes],
        "data":[float(i['total'])for i in incomes]
    }


    return JsonResponse({'expense_data': expense_data, 'income_data': income_data})