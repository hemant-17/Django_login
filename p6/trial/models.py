from django.db import models

# Create your models here.

class Sign(models.Model):
    account_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=150)
    email =  models.CharField(max_length=120)
    password = models.CharField(max_length=10 ,default="NULL")
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=20)
