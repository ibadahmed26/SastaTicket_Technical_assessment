from django.contrib import admin
from .models import User, ResumeModel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "phone_number"]


@admin.register(ResumeModel)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "skill", "experience", "cv"]
