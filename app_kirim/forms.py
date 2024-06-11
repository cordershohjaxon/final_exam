from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea, ChoiceField
from app_users.models import Kirim


class KirimForm(ModelForm):
    class Meta:
        model = Kirim
        fields = ['summa', 'qayerdan', 'tolov_turi', 'ish_haqqi_turi']

