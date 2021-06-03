from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, PasswordInput, Select, FileInput
from UserApp.models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label="username",
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=100, label="email",
                             widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=100, label="first_name",
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, label="last_name",
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
        }


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username': TextInput(attrs={'class': 'input', 'placeholder': 'username'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'email'}),
            'first_name': TextInput(attrs={'class': 'input', 'placeholder': 'first_name'}),
            'last_name': TextInput(attrs={'class': 'input', 'placeholder': 'last_name'}),
        }


CITY = [
    ('Dhaka', 'Dhaka'),
    ('Chattagram', 'Chattagram'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Barishal', 'Barishal'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
    ('Bagerhat', 'Bagerhat'),
    ('Bandarban', 'Bandarban'),
    ('Barguna', 'Barguna'),
    ('Bhola', 'Bhola'),
    ('Bogura', 'Bogura'),
    ('Brahmanbaria', 'Brahmanbaria'),
    ('Chandpur', 'Chandpur'),
    ('Chapainawabganj', 'Chapainawabganj'),
    ('Chuadanga', 'Chuadanga'),
    ("Cox's Bazar", "Cox's Bazar"),
    ('Cumilla', 'Cumilla'),
    ('Dinajpur', 'Dinajpur'),
    ('Faridpur', 'Faridpur'),
    ('Feni', 'Feni'),
    ('Gaibandha', 'Gaibandha'),
    ('Gazipur', 'Gazipur'),
    ('Gopalganj', 'Gopalganj'),
    ('Habiganj', 'Habiganj'),
    ('Jamalpur', 'Jamalpur'),
    ('Jashore', 'Jashore'),
    ('Jhalokati', 'Jhalokati'),
    ('Jhenaidah', 'Jhenaidah'),
    ('Joypurhat', 'Joypurhat'),
    ('Khagrachhari', 'Khagrachhari'),
    ('Kishoreganj', 'Kishoreganj'),
    ('Kurigram', 'Kurigram'),
    ('Kushtia', 'Kushtia'),
    ('Lakshmipur', 'Lakshmipur'),
    ('Lalmonirhat', 'Lalmonirhat'),
    ('Madaripur', 'Madaripur'),
    ('Magura', 'Magura'),
    ('Manikganj', 'Manikganj'),
    ('Meherpur', 'Meherpur'),
    ('Moulvibazar', 'Moulvibazar'),
    ('Munshiganj', 'Munshiganj'),
    ('Naogaon', 'Naogaon'),
    ('Narail', 'Narail'),
    ('Narayanganj', 'Narayanganj'),
    ('Narsingdi', 'Narsingdi'),
    ('Natore', 'Natore'),
    ('Netrokona', 'Netrokona'),
    ('Nilphamari', 'Nilphamari'),
    ('Noakhali', 'Noakhali'),
    ('Pabna', 'Pabna'),
    ('Panchagarh', 'Panchagarh'),
    ('Patuakhali', 'Patuakhali'),
    ('Pirojpur', 'Pirojpur'),
    ('Rajbari', 'Rajbari'),
    ('Rangamati', 'Rangamati'),
    ('Satkhira', 'Satkhira'),
    ('Shariatpur', 'Shariatpur'),
    ('Sherpur', 'Sherpur'),
    ('Sirajganj', 'Sirajganj'),
    ('Sunamganj', 'Sunamganj'),
    ('Tangail', 'Tangail'),
    ('Thakurgaon', 'Thakurgaon'),
]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile()
        fields = ('phone', 'city', 'address', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'phone'}),
            'city': Select(attrs={'class': 'input', 'placeholder': 'city'}, choices=CITY),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'address'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }