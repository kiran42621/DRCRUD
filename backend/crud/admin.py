from django.contrib import admin
from .models import Users

# Register your models here.
@admin.register(Users)
class UsersModel(admin.ModelAdmin):
    list_filter = ('id','name','email')
    list_display = ('id', 'name', 'email')