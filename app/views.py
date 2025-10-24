from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Income, Expense
from decimal import Decimal
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
@login_required(login_url='login')
def index(request):
    data, created = Account.objects.get_or_create(
        user=request.user,
        defaults={'cash': Decimal('0.00')},
    )

    # only show incomes/expenses for the current user
    data1 = Income.objects.filter(user=request.user)
    data2 = Expense.objects.filter(user=request.user)

    if not data1.exists():
        tot_income = Decimal('0.00')
    else:
        tot_income = sum(i.amount for i in data1)

    if not data2.exists():
        tot_expense = Decimal('0.00')
    else:
        tot_expense = sum(e.amount for e in data2)

    context = {
        'data': data,
        'data1': data1,
        'data2': data2,
        'tot_income': tot_income,
        'tot_expense': tot_expense,
    }
    return render(request, 'index.html', context)


@never_cache
@login_required(login_url='login')
def budget(request):
    return render(request,'budget.html')


@never_cache
@login_required(login_url='login')
def transaction(request):
    # get or create per-user account
    data, created = Account.objects.get_or_create(
        user=request.user,
        defaults={'cash': Decimal('0.00')},
    )
    msg = ""

    if request.method == "POST":
        amt = request.POST.get('amt')
        category = request.POST.get('category')
        date = request.POST.get('date')
        desc = request.POST.get('desc')

        if data and amt:
            amt = Decimal(amt)
            if category == "income":
                data.cash += amt
                data.save()
                Income.objects.create(
                    user=request.user,
                    income_type=category,
                    date=date,
                    note=desc,
                    amount=amt,
                )

            elif category == "expense":
                data.cash -= amt
                data.save()
                Expense.objects.create(
                    user=request.user,
                    expense_type=category,
                    date=date,
                    note=desc,
                    amount=amt,
                )
            else:
                msg = "Please Select Category"
                
    data1 = Income.objects.filter(user=request.user)
    data2 = Expense.objects.filter(user=request.user)

    if not data1.exists():
        tot_income = Decimal('0.00')
    else:
        tot_income = sum(i.amount for i in data1)

    if not data2.exists():
        tot_expense = Decimal('0.00')
    else:
        tot_expense = sum(e.amount for e in data2)

    context = {
        'data': data,
        'data1': data1,
        'data2': data2,
        'tot_income': tot_income,
        'tot_expense': tot_expense,
        'msg':msg
    }
    return render(request, 'transaction.html', context)

@never_cache
@require_POST
@login_required
def delete_inc(request, d1):
    # only allow deleting incomes that belong to the user
    item = get_object_or_404(Income, id=d1, user=request.user)
    data = Account.objects.filter(user=request.user).first()
    if data:
        data.cash -= Decimal(item.amount)
        data.save()
    item.delete()
    return redirect('transaction')

@never_cache
@require_POST
@login_required
def delete_exp(request, d2):
    # only allow deleting expenses that belong to the user
    item = get_object_or_404(Expense, id=d2, user=request.user)
    data = Account.objects.filter(user=request.user).first()
    if data:
        data.cash += Decimal(item.amount)
        data.save()
    item.delete()
    return redirect('transaction')

@never_cache
@login_required(login_url='login')
def chart(request):
    return render(request,'chart.html')

@never_cache
@login_required(login_url='login')
def chart_data(request):
    expenses=Expense.objects.all()
    incomes=Income.objects.all()

    expense_data={
        "labels":[f"{e.expense_type} - {e.note}" for e in expenses],
        "data":[float(e.amount)for e in expenses]
    }

    income_data={
        "labels":[f"{i.income_type} - {i.note}"for i in incomes],
        "data":[float(i.amount)for i in incomes]
    }
    return JsonResponse({'expense_data': expense_data, 'income_data': income_data})