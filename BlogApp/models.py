from django.db import models
from ProductApp.models import Category
from django.utils.safestring import mark_safe


# Create your models here.
class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='blog')
    blog_short = models.CharField(max_length=250)
    blog_details = models.TextField()
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" height="50" width="40"/>'.format(self.image.url))

    image_tag.short_description = "Image"