from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField(max_length=20)
class Employee(models.Model):
    ename=models.CharField(max_length=100)
    emailid=models.EmailField()
    password=models.CharField(max_length=20)
    course=models.ForeignKey(Department)

