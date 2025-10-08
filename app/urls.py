from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='dashboard'),
    path('chart/',views.chart,name='chart'),
    path('budget/',views.budget,name="budget"),
    path('transaction/',views.transaction,name="transaction"),
    path('delete/income/<int:d1>',views.delete_inc,name="delete1"),
    path('delete/expense/<int:d2>',views.delete_exp,name='delete2'),
]