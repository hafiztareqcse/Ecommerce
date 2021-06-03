from django.db import models
from django.forms import ModelForm, TextInput, EmailInput


# Create your models here.
class Setting(models.Model):
    STATUS = (('True', 'True'),
              ('False', 'False'),
              )
    title = models.CharField(max_length=264)
    keyword = models.CharField(max_length=264)
    details = models.TextField()
    description = models.TextField()
    address = models.CharField(max_length=264)
    phone = models.IntegerField()
    email = models.EmailField(max_length=264, blank=True, null=True)
    smptserver = models.CharField(max_length=264, blank=True, null=True)
    smptemail = models.EmailField(max_length=264, blank=True, null=True)
    smptpassword = models.CharField(blank=True, max_length=264)
    smptport = models.CharField(blank=True, max_length=264)
    icon = models.ImageField(blank=True, null=True, upload_to="icon")
    facebook = models.CharField(blank=True, max_length=264)
    twitter = models.CharField(blank=True, max_length=264)
    instagram = models.CharField(blank=True, max_length=264)
    linkedin = models.CharField(blank=True, max_length=264)
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def imageurl(self):
        if self.icon:
            return self.icon.url
        else:
            return ""


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    ip = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Your Name'}),
            'email': EmailInput(attrs={'class': 'input', 'placeholder': 'Your Email'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'message': TextInput(attrs={'class': 'input', 'placeholder': 'Write Message'}),
        }


class OurTeam(models.Model):
    name = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to="our_team")
    facebook = models.CharField(blank=True, max_length=264)
    twitter = models.CharField(blank=True, max_length=264)
    instagram = models.CharField(blank=True, max_length=264)
    linkedin = models.CharField(blank=True, max_length=264)

    def __str__(self):
        return self.name

    def imageurl(self):
        if self.image:
            return self.image.url
        else:
            return ""
