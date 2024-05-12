from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea
from django.contrib.auth import get_user_model
from django import forms

from .models import Note

User = get_user_model()


class UserRegistrationForm(ModelForm):
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'block text-sm font-medium text-gray-700 mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
            }),
            'last_name': TextInput(attrs={
                'class': 'block text-sm font-medium text-gray-700 mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'username': TextInput(attrs={
                'class': 'block text-sm font-medium text-gray-700 mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
            'email': EmailInput(attrs={
                'class': 'block text-sm font-medium text-gray-700 mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
            }),
        }


class NoteForm(ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'owner', 'description']
        widgets = {
            'title': TextInput(attrs={
                'class': 'block text-sm font-medium text-gray-700 mt-1 p-2 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500',
            }),
            'description': Textarea(attrs={
                'class': 'p-3 bg-white border border-gray-200 rounded shadow h-20 w-full '
            }),

        }
