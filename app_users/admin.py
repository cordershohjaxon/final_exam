from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from .models import Kirim, Chiqim

User = get_user_model()


class KirimAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'summa', 'qayerdan', 'sana', 'tolov_turi', 'ish_haqqi_turi')
    list_filter = ('sana', 'user', 'tolov_turi', 'ish_haqqi_turi')
    search_fields = ('qayerdan',)


class ChiqimAdmin(admin.ModelAdmin):
    list_display = ('user', 'summa', 'qayerga', 'tolov_turi', 'chiqim_turi', 'sana')
    list_filter = ('tolov_turi', 'chiqim_turi', 'sana')
    search_fields = ('user__username', 'qayerga', 'tolov_turi', 'chiqim_turi')
    ordering = ('-sana',)
    fields = ('user', 'summa', 'qayerga', 'tolov_turi', 'chiqim_turi', 'sana')


admin.site.register(Chiqim, ChiqimAdmin)
admin.site.register(Kirim, KirimAdmin)
admin.site.register(User)
admin.site.unregister(Group)
