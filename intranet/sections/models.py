from django.db import models
from django.contrib.auth import get_user_model


class Section(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	description = models.TextField(blank=True)
	parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
	is_private = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name
