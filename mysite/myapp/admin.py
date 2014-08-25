from django.contrib import admin
from myapp.models import Student,Contact
from employee.models import Department,Employee
class ContactInline(admin.TabularInline):
    model = Contact
    extra = 3

class StudentAdmin(admin.ModelAdmin):
    #fields=['rollno','sname']
    fieldsets = [
        (None,{'fields':['sname','join_date']}),
        ('Student ROLL NO...',{
            'fields':['rollno'],
            'classes':['collapse'],
        }),
    ]
    list_display = ('sname','rollno','join_date')
    list_filter = ('rollno','id')
    list_per_page = 3
    inlines = [ContactInline]

class DepartmentAdmin(admin.ModelAdmin):
    fields = ['dname']
    list_display = ('dname',)
    list_filter = ('id',)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ['ename','emailid','mobno']
    list_display = ('ename','emailid','mobno')
    list_filter = ('ename','emailid','mobno')
# Register your models here.
admin.site.register(Student,StudentAdmin)#display Rollno First in Admin site.StudentAdmin id admin model class it's Second argumant of register()
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
#admin.site.register(Contact)
#admin.site.register(Student)
