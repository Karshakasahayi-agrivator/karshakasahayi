from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    address=models.CharField(max_length=2000)
    workers=models.IntegerField()
    date_required=models.DateField()
