from django.contrib import admin
from .models import Role, SectionMembership


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	list_display = ("name", "description")
	search_fields = ("name",)


@admin.register(SectionMembership)
class SectionMembershipAdmin(admin.ModelAdmin):
	list_display = ("user", "section", "permission", "role", "created_at")
	list_filter = ("permission", "section")
	search_fields = ("user__username", "section__name")
