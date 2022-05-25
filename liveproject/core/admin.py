from django.contrib import admin
from .models import CustomUser, Vacation

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Vacation)
