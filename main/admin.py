from django.contrib import admin
from .models import (
    SponsorModel,
    StudentModel,
    UniversityModel,
    SponsorshipModel,
)


@admin.register(SponsorModel)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'father_name', 'enter_money', 'created_date']
    list_filter = ['enter_money', 'company_name']
    search_fields = ['first_name', 'enter_money', 'company']
    ordering = ['enter_money']


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'university', 'contract']
    list_filter = ['first_name', 'university', 'contract', 'created_date']
    search_fields = ['first_name', 'university', 'contract']
    ordering = ['contract']


@admin.register(UniversityModel)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_date']
    search_fields = ['name', 'created_date']
    ordering = ['created_date']


@admin.register(SponsorshipModel)
class SponsorshipAdmin(admin.ModelAdmin):
    list_display = ['sponsor', 'student', 'money', 'created_date']
    search_fields = ['sponsor', 'student']
    ordering = ['created_date']
