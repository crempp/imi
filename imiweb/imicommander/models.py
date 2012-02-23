from django.db import models

# Create your models here.

class Command(models.Model):
	name        = models.CharField(max_length=32)
	description = models.TextField(blank=True)