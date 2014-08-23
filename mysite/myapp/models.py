from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=100)
    rollno=models.IntegerField(default=0)
    join_date=models.DateTimeField("Joining Date")
    #exam_no=models.IntegerField()
    def __unicode__(self):
        return self.sname
    def was_join_recently(self):
        now=timezone.now()
        return now - datetime.timedelta(days=1) <= self.join_date <= now
    was_join_recently.admin_order_field = 'join_date'
    was_join_recently.boolean = True
    was_join_recently.short_description = 'Join recently?'
class Contact(models.Model):
    address=models.CharField(max_length=200)
    stdno=models.BigIntegerField()
    student=models.ForeignKey(Student)
    def __unicode__(self):
        return self.address