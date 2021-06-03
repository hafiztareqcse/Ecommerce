from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class Category(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title = models.CharField(max_length=264)
    keywords = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='category')
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""


class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=264)
    keywords = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='product')
    new_price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    old_price = models.DecimalField(decimal_places=2, max_digits=20)
    amount = models.IntegerField(default=0)
    min_amount = models.IntegerField(default=2)
    details = models.TextField()
    status = models.CharField(max_length=50, choices=status)
    slug = models.SlugField(null=True, unique=True)
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

    def get_absolute_url(self):
        return reverse('product_element', kwargs={'slug': self.slug})


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=264, blank=True)
    image = models.ImageField(blank=True, upload_to='product')

    def __str__(self):
        return self.title


class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200, blank=True)
    comment = models.CharField(max_length=1000, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, default='New')
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
