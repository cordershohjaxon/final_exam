from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Note

User = get_user_model()

admin.site.register(User)
admin.site.unregister(Group)
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created', 'updated')
    search_fields = ('title', 'owner')
    list_filter = ('created', 'updated')
    list_per_page = 50
    list_display_links = ('title',)
