from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    cash=models.DecimalField(default=0,max_digits=9,decimal_places=2)

    # def __str__(self):
    #     return str(self.cash)
    
class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    expense_type=models.CharField(max_length=32)
    date=models.DateField()
    note=models.TextField(max_length=100)
    amount=models.DecimalField(max_digits=9,decimal_places=2)

class Income(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    income_type=models.CharField(max_length=32)
    date=models.DateField()
    note=models.TextField(max_length=100)
    amount=models.DecimalField(max_digits=9,decimal_places=2)