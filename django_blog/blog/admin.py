from django.contrib import admin
from .models import Post, Comment

# Register Post with tags
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date")
    list_filter = ("author", "published_date")
    search_fields = ("title", "content")

# Register Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "created_at", "updated_at")
    search_fields = ("content", "author__username", "post__title")
