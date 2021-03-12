from django.contrib import admin

from .models import BlogAuthor, BlogCategory, BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogAuthor)
class BlogAuthor(admin.ModelAdmin):
    pass
