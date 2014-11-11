from django.contrib import admin
from .models import Post

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'published_date')

admin.site.register(Post, AuthorAdmin)
