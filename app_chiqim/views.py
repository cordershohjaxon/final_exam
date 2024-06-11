from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from app_users.models import Chiqim
from .forms import ChiqimForm

class ChiqimListView(LoginRequiredMixin, ListView):
    model = Chiqim
    template_name = 'app_chiqim/chiqim_page.html'
    context_object_name = 'chiqimlar'

    def get_queryset(self):
        return Chiqim.objects.filter(user=self.request.user)


class ChiqimCreateView(LoginRequiredMixin, CreateView):
    model = Chiqim
    form_class = ChiqimForm
    template_name = 'app_chiqim/chiqim_form.html'
    success_url = reverse_lazy('chiqim_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChiqimUpdateView(LoginRequiredMixin, UpdateView):
    model = Chiqim
    form_class = ChiqimForm
    template_name = 'app_chiqim/chiqim_form.html'
    success_url = reverse_lazy('chiqim_page')

    def get_queryset(self):
        return Chiqim.objects.filter(user=self.request.user)


class ChiqimDeleteView(LoginRequiredMixin, DeleteView):
    model = Chiqim
    template_name = 'app_chiqim/chiqim_delete.html'
    success_url = reverse_lazy('chiqim_page')

    def get_queryset(self):
        return Chiqim.objects.filter(user=self.request.user)