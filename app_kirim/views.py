from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from app_users.models import Kirim, User

from .forms import KirimForm


class KirimListView(LoginRequiredMixin, ListView):
    model = Kirim
    template_name = 'app_kirim/kirim_page.html'
    context_object_name = 'kirimlar'

    def get_queryset(self):
        return Kirim.objects.filter(user=self.request.user)


class KirimCreateView(LoginRequiredMixin, CreateView):
    model = Kirim
    form_class = KirimForm
    template_name = 'app_kirim/kirim_create.html'
    success_url = reverse_lazy('kirim_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class KirimUpdateView(LoginRequiredMixin, UpdateView):
    model = Kirim
    form_class = KirimForm
    template_name = 'app_kirim/kirim_create.html'
    success_url = reverse_lazy('kirim_page')

    def get_queryset(self):
        return Kirim.objects.filter(user=self.request.user)


class KirimDeleteView(LoginRequiredMixin, DeleteView):
    model = Kirim
    template_name = 'app_kirim/kirim_delete.html'
    success_url = reverse_lazy('kirim_page')

    def get_queryset(self):
        return Kirim.objects.filter(user=self.request.user)
