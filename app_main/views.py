from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()


@login_required(login_url='login')
def home_page(request):

    full_name = request.user.get_full_name()
    context = {
        "full_name": full_name,
    }

    return render(request, 'app_main/home.html', context)


