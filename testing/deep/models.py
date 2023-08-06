from django.db import models

# Create your models here.
class Plans(models.Model):
    Plan_Name=models.CharField(max_length=50)
    Mobile=models.IntegerField()
    Basic=models.IntegerField()
    Standard=models.IntegerField()
    Premium=models.IntegerField()

class current_plan(models.Model):
    plan_type=models.CharField(max_length=50)
    Plan_Name=models.CharField(max_length=50)
    price=models.IntegerField()
    subscription=models.CharField(max_length=10)
