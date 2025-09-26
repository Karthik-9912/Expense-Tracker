from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField(unique=True)
    phone=models.PositiveBigIntegerField(unique=True)

    # def __str__(self):
    #     return self.name