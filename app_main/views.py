from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from app_users.models import Kirim, Chiqim

User = get_user_model()


@login_required(login_url='login')
def home_page(request):
    """
    Renders the home page with a combined list of 'Kirim' and 'Chiqim' objects for the logged-in user.

    This view requires the user to be logged in. It fetches 'Kirim' and 'Chiqim' objects related to the logged-in user,
    combines them into a single list, and passes this list along with the user's full name to the template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object with the rendered template.
    """
    list1 = Kirim.objects.filter(user=request.user)
    list2 = Chiqim.objects.filter(user=request.user)
    royxat = []

    for i in list1:
        royxat.append(i)

    for j in list2:
        royxat.append(j)

    full_name = request.user.get_full_name()
    context = {
        "full_name": full_name,
        'royxat': royxat
    }

    return render(request, 'app_main/home.html', context)
