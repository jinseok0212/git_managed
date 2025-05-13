from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('추가정보', {'fields': ('nickname', 'age')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('추가정보', {'fields': ('nickname', 'age')}),
    )
    
    list_display = ['username', 'email', 'nickname', 'age']

admin.site.register(CustomUser, CustomUserAdmin)