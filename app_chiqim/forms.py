from django import forms

from app_users.models import Chiqim


class ChiqimForm(forms.ModelForm):
    class Meta:
        model = Chiqim
        fields = ['summa', 'qayerga', 'tolov_turi', 'chiqim_turi',]
        widgets = {}

