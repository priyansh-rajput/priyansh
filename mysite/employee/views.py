from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from employee.models import Department,Employee
import smtplib
from myapp.models import Contact
# Create your views here.
def registration(request):
    dept_list=Department.objects.order_by('dname')
    return HttpResponse(render(request,'employee/Registration.html',{'dept_list':dept_list,}))
def employeeInsert(request):
    emp=Employee()
    emp.ename=request.POST['ename']
    emp.emailid=request.POST['emailid']
    emp.password=request.POST['password']
    emp.department_id=request.POST['dept']
    emp.mobno=request.POST['mobno']
    emp.save()
    return HttpResponse(render(request,'employee/Login.html',))
def employeeLogin(request):
    try:
        emp1 = Employee.objects.get(emailid=request.POST['emailid'])
        if(emp1.password != request.POST['password']):
            return render(request,'employee/Login.html',{'errorMessage':'Invalid Email Or/And Password...!'})
        elif(emp1.password == request.POST['password']):
            request.session["emp"]=emp1.ename
            return HttpResponse(render(request,'employee/Home.html',{'request':request}))
    except Employee.DoesNotExist:
        return render(request,'employee/Login.html',{'errorMessage':'Invalid Email Or/And Password...!'})
def moveLogin(request):
    return(render(request,'employee/Login.html',))
def moveForgotPassword(request):
    return(render(request,'employee/forgotPassword.html',))
def forgotPassword(request):
    try:
        emp=Employee.objects.get(mobno=request.POST['mobno'])
        if(emp!=None):
            Toid=emp.emailid
            fromid='practiciatest@gmail.com'
            message="hi %s Your Employee Detail's Password is %s"%(emp.ename,emp.password)
            obj=smtplib.SMTP('smtp.gmail.com:587')
            obj.starttls()
            obj.login(fromid,'Promact2013')
            obj.sendmail(fromid,Toid,message)
            obj.quit()
            return render(request,'employee/forgotPassword.html',{'conMessage':'Yor Password Send On Your Register Email ID....'})
    except Employee.DoesNotExist:
        return render(request,'employee/forgotPassword.html',{'conMessage':'Mobile Number Not Register..!'})
def logout(request):
    try:
        del request.session['emp']
    except KeyError:
        pass
    return render(request,'employee/logout.html',)
def moveLogout(request):
    return render(request,'employee/logout.html',)