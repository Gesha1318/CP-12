from django.contrib import admin
from .models import Article, File


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "is_published", "created_at")
	list_filter = ("section", "is_published")
	search_fields = ("title", "slug", "content")
	prepopulated_fields = {"slug": ("title",)}


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
	list_display = ("title", "section", "created_at")
	list_filter = ("section",)
	search_fields = ("title",)
