from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from app_users.models import Chiqim
from .forms import ChiqimForm


class ChiqimListView(LoginRequiredMixin, ListView):
    """
    View to list all 'Chiqim' objects for the logged-in user.

    Inherits:
        LoginRequiredMixin: Mixin that ensures the user is logged in.
        ListView: A Django class-based view to list objects.

    Attributes:
        model (Chiqim): The model to list.
        template_name (str): The path to the template used to render the view.
        context_object_name (str): The name of the context variable that will contain the queryset.
    """

    model = Chiqim
    template_name = 'app_chiqim/chiqim_page.html'
    context_object_name = 'chiqimlar'

    def get_queryset(self):
        """
        Returns the queryset of 'Chiqim' objects for the logged-in user.
        """
        return Chiqim.objects.filter(user=self.request.user)


class ChiqimCreateView(LoginRequiredMixin, CreateView):
    """
    View to create a new 'Chiqim' object.

    Inherits:
        LoginRequiredMixin: Mixin that ensures the user is logged in.
        CreateView: A Django class-based view to create objects.

    Attributes:
        model (Chiqim): The model to create.
        form_class (ChiqimForm): The form class used to create the object.
        template_name (str): The path to the template used to render the view.
        success_url (str): The URL to redirect to on successful form submission.
    """

    model = Chiqim
    form_class = ChiqimForm
    template_name = 'app_chiqim/chiqim_form.html'
    success_url = reverse_lazy('chiqim_page')

    def form_valid(self, form):
        """
        Set the user of the 'Chiqim' object to the logged-in user before saving the form.

        Args:
            form (ChiqimForm): The form instance being validated.

        Returns:
            HttpResponse: The response to be sent to the client.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class ChiqimUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update an existing 'Chiqim' object.

    Inherits:
        LoginRequiredMixin: Mixin that ensures the user is logged in.
        UpdateView: A Django class-based view to update objects.

    Attributes:
        model (Chiqim): The model to update.
        form_class (ChiqimForm): The form class used to update the object.
        template_name (str): The path to the template used to render the view.
        success_url (str): The URL to redirect to on successful form submission.
    """

    model = Chiqim
    form_class = ChiqimForm
    template_name = 'app_chiqim/chiqim_form.html'
    success_url = reverse_lazy('chiqim_page')

    def get_queryset(self):
        """
        Returns the queryset of 'Chiqim' objects for the logged-in user.
        """
        return Chiqim.objects.filter(user=self.request.user)


class ChiqimDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete an existing 'Chiqim' object.

    Inherits:
        LoginRequiredMixin: Mixin that ensures the user is logged in.
        DeleteView: A Django class-based view to delete objects.

    Attributes:
        model (Chiqim): The model to delete.
        template_name (str): The path to the template used to render the view.
        success_url (str): The URL to redirect to on successful form submission.
    """

    model = Chiqim
    template_name = 'app_chiqim/chiqim_delete.html'
    success_url = reverse_lazy('chiqim_page')

    def get_queryset(self):
        """
        Returns the queryset of 'Chiqim' objects for the logged-in user.
        """
        return Chiqim.objects.filter(user=self.request.user)
