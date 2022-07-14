from django.contrib import admin
from myapp.models import Employee

# Register your models here.
@admin.register(Employee)

class EmployeeAdmin(admin.ModelAdmin):
      list_display=['idno','name','contact','email','salary','address']
