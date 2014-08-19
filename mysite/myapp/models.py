from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100)
    rollno=models.IntegerField(default=0)
    def __unicode__(self):
        return self.sname
class Contact(models.Model):
    address=models.CharField(max_length=200)
    stdno=models.BigIntegerField()
    student=models.ForeignKey(Student)
    def __unicode__(self):
        return self.address