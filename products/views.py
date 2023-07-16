from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ProductDetailPage
from django.contrib.auth import get_user_model

UserModel = get_user_model()

# Was using csrf_exempt to test ajax post, 
# found out I could just send the csrf_token data through csrfmiddlewaretoken

# @csrf_exempt
def registerProduct(request):
    if request.POST:
        page_id = request.POST['page']
        user_id = request.POST['user']
        page = ProductDetailPage.objects.get(id=page_id)
        user = UserModel.objects.get(id=user_id)
        page.registered_users.add(user)

    # haven't decided what to put here, 
    # the code works, so I'm just leaving this as is :)
    return HttpResponse("user registered")