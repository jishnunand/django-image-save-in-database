from django.contrib import admin

# Register your models here.
from employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Employee, EmployeeAdmin)