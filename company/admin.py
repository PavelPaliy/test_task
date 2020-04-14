from django.contrib import admin

# Register your models here.
from .models import Main, About, Contacts
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group


class MainAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    list_display = ('title',)
    list_display_links = ('title',)
    show_delete_link = False
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AboutAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    list_display = ('title',)
    list_display_links = ('title',)
    show_delete_link = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

class ContactsAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    list_display = ('title',)
    list_display_links = ('title',)
    show_delete_link = False

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Main, MainAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
