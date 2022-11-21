import re

from django.shortcuts import render, redirect
from django.urls import reverse
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

def register(request):
    '''Access register page'''
    return render(request, 'register.html')


def register_handle(request):
    '''Process register'''
    # accept data
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    # check data
    if not all([username, password, email]):
        # lack data

        return render(request, 'register.html', {'errmsg': 'Lack information'})

    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': 'Email Error'})
    if allow != 'on':
        return render(request, 'register.html', {'errmsg': 'Please allow agreement'})
    print(123123)
    # process:create account
    user = User.objects.create_user(username, email, password)
    user.save()
    print(456456)
    # response, jump to front page
    return redirect(reverse('goods:index'))