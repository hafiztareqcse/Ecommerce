from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ProductApp.models import Product, Category, Images
from MainApp.models import Setting
from django.contrib import messages
from UserApp.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from UserApp.models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('MainApp:home')
        else:
            messages.warning(request, 'Username or password is incorrect')
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
    }
    return render(request, 'login.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = 'user_pic/avatar.png'
            data.save()
            return redirect('MainApp:home')
        else:
            messages.warning(request, 'Password and confirm password is not matching')
    else:
        form = RegisterForm()

    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    context = {
        'setting': setting,
        'category': category,
        'form': form
    }
    return render(request, 'register.html', context)


def user_profile(request):
    setting = Setting.objects.get(id=1)
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'setting': setting,
        'category': category,
        'profile': profile
    }
    return render(request, 'user-profile.html', context)


@login_required(login_url='/user/login/')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('UserApp:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, 'user-update.html', context)

@login_required(login_url='/user/login/')
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password is successfully changed!')
            return redirect('UserApp:profile')
        else:
            messages.error(request, 'Please correct the error <br>'+ str(form.errors))
            return redirect('UserApp:password')
    else:
        setting = Setting.objects.get(id=1)
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        context = {
            'setting': setting,
            'category': category,
            'form': form
        }
        return render(request, 'password-change.html', context)

def user_logout(request):
    logout(request)
    return redirect('MainApp:home')
