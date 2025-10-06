from django.db import models

# Create your models here.
class Account(models.Model):
    cash=models.DecimalField(default=0,max_digits=9,decimal_places=2)

    def __str__(self):
        return str(self.cash)
    
class Expense(models.Model):
    expense_type=models.CharField(max_length=32)
    date=models.DateField()
    note=models.TextField(max_length=100)
    amount=models.DecimalField(max_digits=9,decimal_places=2)

class Income(models.Model):
    income_type=models.CharField(max_length=32)
    date=models.DateField()
    note=models.TextField(max_length=100)
    amount=models.DecimalField(max_digits=9,decimal_places=2)