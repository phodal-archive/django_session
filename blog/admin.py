from django.contrib import admin
from blog.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'date',)

admin.site.register(Blog, BlogAdmin)
