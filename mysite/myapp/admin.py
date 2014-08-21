from django.contrib import admin
from myapp.models import Student,Contact
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
# Register your models here.
admin.site.register(Student,StudentAdmin)#display Rollno First in Admin site.StudentAdmin id admin model class it's Second argumant of register()
#admin.site.register(Contact)
#admin.site.register(Student)
