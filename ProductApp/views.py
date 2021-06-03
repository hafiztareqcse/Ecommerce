from django.shortcuts import render, HttpResponseRedirect
from MainApp.models import Setting
from ProductApp.models import Category, Product, Images, Comment, CommentForm
from django.contrib import messages

def product_single(request, id):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    context = {
        'setting': setting,
        'category': category,
        'single_product': single_product,
        'images': images
    }
    return render(request, 'single-product.html', context)


def category_product(request, id, slug):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    product_category = Product.objects.filter(category_id=id)
    product_details = Product.objects.get(id=id)
    context = {'setting': setting,
               'category': category,
               'product_details': product_details,
               'product_category': product_category, }
    return render(request, 'category-product.html', context)


def comment_add(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommentForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.subject = pos.cleaned_data['subject']
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'Your informative comment has been sent')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)