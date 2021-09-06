from django.contrib import admin
from schoolinfo import models
from .models import *

# Register your models here.
admin.site.register(department)
admin.site.register(course_year)
admin.site.register(students)
admin.site.register(professor)