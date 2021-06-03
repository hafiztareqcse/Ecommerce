from django.contrib import admin
from ProductApp.models import Category, Product, Images, Comment

admin.site.register(Category)


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at', 'updated_at', 'image_tag']
    list_filter = ['title', 'created_at']
    list_per_page = 10
    search_fields = ['title', 'new_price', 'details']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]


admin.site.register(Product, ProductAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'status', 'created_at', 'updated_at', 'user']
    list_filter = ['status', 'created_at']
    list_per_page = 10


admin.site.register(Comment, CommentAdmin)
