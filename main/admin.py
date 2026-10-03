from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'nickname', 'hometown', 'year_level', 'favorite_subject', 'club')
    list_filter = ('year_level', 'club')
    search_fields = ('name', 'nickname', 'hometown')
