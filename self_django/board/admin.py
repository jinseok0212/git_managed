from django.contrib import admin
from .models import Post, Comment





class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_at', 'post']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

