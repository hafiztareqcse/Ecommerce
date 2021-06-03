from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from MainApp.models import Setting, ContactForm, ContactMessage, OurTeam
from ProductApp.models import Product, Category, Images
from django.contrib import messages
from MainApp.forms import SearchForm
from OrderApp.models import Cart, CartForm
from BlogApp.models import Blog


def home(request):
    current_user = request.user
    cart_product = Cart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    latest_product = Product.objects.all().order_by('-id')
    featured_product = Product.objects.all()
    latest_blog = Blog.objects.all().order_by('-id')
    context = {
        'setting': setting,
        'category': category,
        'latest_product': latest_product,
        'featured_product': featured_product,
        'cart_product': cart_product,
        'total_amount': total_amount,
        'latest_blog': latest_blog
    }
    return render(request, 'index.html', context)


def about(request):
    current_user = request.user
    cart_product = Cart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    our_team = OurTeam.objects.all()
    context = {
        'setting': setting,
        'category': category,
        'our_team': our_team,
        'cart_product': cart_product,
        'total_amount': total_amount,
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE ADDR')
            data.save()
            messages.success(request, 'Your message has been sent')
            return HttpResponseRedirect(reverse('MainApp:contact'))
    form = ContactForm
    current_user = request.user
    cart_product = Cart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
        'form': form,
        'cart_product': cart_product,
        'total_amount': total_amount,
    }
    return render(request, 'contact.html', context)


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            category = form.cleaned_data['category']
            if category == 0:
                products = Product.objects.filter(title__icontains=query)
            else:
                products = Product.objects.filter(title__icontains=query, category_id=category)
            category = Category.objects.all()
            context = {
                'category': category,
                'query': query,
                'product_category': products
            }
            return render(request, 'category-product.html', context)
    return HttpResponseRedirect(reverse('ProductApp:category-product'))
