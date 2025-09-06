from django.contrib import admin
from .models import Contact, Project

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "number", "email_title", "created_at")
    search_fields = ("name", "email", "email_title")
    list_filter = ("created_at",)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "short_description", "link")
    search_fields = ("title", "short_description", "long_description")
    list_filter = ("title",)