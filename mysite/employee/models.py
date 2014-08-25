from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=100)
class Employee(models.Model):
    ename=models.CharField(max_length=150)
    emailid=models.EmailField()
    password=models.CharField(max_length=20)
    mobno=models.BigIntegerField()
    department=models.ForeignKey(Department)
