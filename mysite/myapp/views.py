from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from myapp.models import Student,Contact
from django.template import RequestContext,loader
# Create your views here.
def index(request):
    all_stud_list=Student.objects.order_by("sname")
    #out=",".join([s.sname for s in all_student_list])
    template=loader.get_template('myapp/index.html')
    context=RequestContext(request,{'all_stud_list':all_stud_list,})
     #return render(request, 'myapp/index.html', context) no need to load Template thought loader this method return HttpResponse
    return HttpResponse(template.render(context))

def detail(request,student_id):

    #try:
     #   stud=Student.objects.get(pk=student_id)
    #except stud.DoesNotExist:
     #   raise Http404
    stud=get_object_or_404(Student,pk=student_id)#Shortcut Method for above comment code and it raises Http404 if the list is empty.
    return render(request,'myapp/detail.html',{'stud':stud})#return HttpResponse

    return HttpResponse("YoU Are Looking in Student:%s"%student_id)
def result(request,student_id):
    return HttpResponse("You Are Looking in Result of student ::%s"%student_id)
def contact(request,student_id):
    return HttpResponse("You Are Contact In Student::%s"%student_id)
