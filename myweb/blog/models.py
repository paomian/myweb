from django.db import models
from django.contrib import admin
# Create your models here.
class blog(models.Model):
	title = models.CharField('title',max_length=40)
	content = models.TextField('content',max_length=2000)
	time = models.DateTimeField('edit date')

class blogadmin(admin.ModelAdmin):
	list_display = ('title','time')
