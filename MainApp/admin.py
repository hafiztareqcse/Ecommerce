from django.contrib import admin
from MainApp.models import Setting, ContactMessage, OurTeam

# Register your models here.
admin.site.register(Setting)
admin.site.register(ContactMessage)


class OurTeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'status']
    list_filter = ['status']


admin.site.register(OurTeam, OurTeamAdmin)
