from django.contrib import admin

# Register your models here.
class Department(admin.ModelAdmin):
    fields = ['dname']
list_display = ('dname')
list_filter = ('dname')
admin.site.register(Department)