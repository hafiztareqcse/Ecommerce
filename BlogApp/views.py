from django.shortcuts import render
from BlogApp.models import Blog
from MainApp.models import Setting, ContactForm, ContactMessage, OurTeam
from ProductApp.models import Product, Category, Images


# Create your views here.

def blog(request):
    blog_info = Blog.objects.all()
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
        'blog_info': blog_info,
    }
    return render(request, 'blog.html', context)

def blog_details(request):
    blog_info = Blog.objects.get(id=1)
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
        'blog_info': blog_info,
    }
    return render(request, 'blog-details.html', context)

