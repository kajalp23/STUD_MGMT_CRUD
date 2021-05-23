from django.contrib import admin
from student.models import Stud

@admin.register(Stud)
class StudAdmin(admin.ModelAdmin):
    list_display=['name','email','password']

# Register your models here.
