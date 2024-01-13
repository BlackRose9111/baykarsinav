from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UAVCategory)
admin.site.register(models.UAV)
admin.site.register(models.Rent)
