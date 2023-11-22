from django.contrib import admin
from .import models

# Register your models here.
admin.site.register(models.Department)
admin.site.register(models.Degreeprogram)
admin.site.register(models.Semester)
admin.site.register(models.Subject)
admin.site.register(models.Faculty)
admin.site.register(models.TimetableData)
admin.site.register(models.Admin)
