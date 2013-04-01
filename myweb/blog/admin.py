from django.contrib import admin
from myweb.blog.models import blog, blogadmin

admin.site.register(blog,blogadmin)
