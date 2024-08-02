from typing import Optional
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Seeker, Csv


@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'company', 'position', 'seeker']
    search_fields = ['first_name', 'last_name', 'company', 'position', 'seeker__first_name', 'seeker__last_name']
    list_per_page = 20
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    
class CsvInline(admin.TabularInline):
    model = Csv
    extra = 0


@admin.register(Seeker)
class SeekerAdmin(UserAdmin):
    model = Seeker
    
    inlines = [CsvInline]
    
    def get_displayed_password(self, instance):
        return '********'
    
    list_display = ['username', 'first_name', 'last_name', 'created_at', 'referrer']
    list_filter =  ['referrer']
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ['-created_at']
    list_per_page = 50
    
    fieldsets = (
        (None, {
                'fields': ('username', 'password')
            }),
        ('Personal info', {
                'fields': ('first_name', 'last_name', 'email', 'referrer')
            }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    