from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
User = get_user_model()


def user_registration(request):
    """
    Handles user registration by creating a new user if the provided data is valid.

    This view handles the user registration process. If the request method is POST,
    it retrieves the form data, checks if the passwords match, and if the email is
    not already registered. If the validation passes, a new user is created and redirected
    to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template or a redirect to the login page.
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if password1 == password2 and not user:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            user.set_password(password2)
            user.save()
            return redirect('login')

    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/registration.html', context)


def login_user(request):
    """
    Handles user login by authenticating and logging in the user.

    This view handles the user login process. If the request method is POST, it
    retrieves the username and password, checks if the user exists and the password
    is correct, and logs in the user if the validation passes. It then redirects the
    user to the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template or a redirect to the home page.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            user_exists = user.check_password(password)
        except:
            user_exists = None
            user = None

        if user_exists:
            login(request, user)
            return redirect('home')
    return render(request, 'app_users/login.html')


def logout_user(request):
    """
    Logs out the current user and redirects to the login page.

    This view handles the user logout process. It logs out the currently logged-in
    user and redirects them to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the login page.
    """
    logout(request)
    return redirect('login')
