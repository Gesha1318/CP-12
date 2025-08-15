from django.db import models
from django.contrib.auth import get_user_model
from sections.models import Section


def upload_to_article(instance, filename):
	return f"articles/{instance.section.slug}/{filename}"


def upload_to_file(instance, filename):
	return f"files/{instance.section.slug}/{filename}"


class Article(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='articles')
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255)
	content = models.TextField()
	author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
	is_published = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		unique_together = ('section', 'slug')
		ordering = ['-created_at']

	def __str__(self):
		return self.title


class File(models.Model):
	section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='files')
	title = models.CharField(max_length=255)
	file = models.FileField(upload_to=upload_to_file)
	uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
