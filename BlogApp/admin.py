from django.contrib import admin
from BlogApp.models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at', 'image_tag']
    list_filter = ['category']


admin.site.register(Blog, BlogAdmin)
