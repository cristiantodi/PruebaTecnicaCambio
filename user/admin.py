from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):   
    pass