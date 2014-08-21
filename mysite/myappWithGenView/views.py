from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from myapp.models import Student,Contact
from django.views import generic
# Create your views here.
#Creating Generic view For Student and Contact models from myapp
#the work of this views are same myapp's views But use Generic view
#this views use models from myapp/models.py
class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = "all_stud_list"
    def get_queryset(self):
        "Return All Student Records."
        return Student.objects.order_by('sname')
class DetailView(generic.DetailView):
    model = Student#shorthand for queryset=Student.objects.all()
    context_object_name = 'stud'
    template_name = 'myapp/detailForm.html'
class ResultView(generic.DetailView):
    model = Student#shorthand for queryset=Student.objects.all()
    context_object_name = 'stud'
    template_name = 'myapp/result.html'