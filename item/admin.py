from django.contrib import admin

# Register your models here.
from .models import category,item
admin.site.register(category)
admin.site.register(item)