from django.contrib import admin
from .models import Section


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	list_display = ("name", "parent", "is_private")
	search_fields = ("name", "slug")
	prepopulated_fields = {"slug": ("name",)}
