import re
from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

User = get_user_model()


# Create your views here.

class register_view(View):
    '''REGISTER'''

    def get(self, request):
        '''Show Register'''
        return render(request, 'register.html')

    def post(self, request):
        '''Process Register'''
        # Process register
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
        # check id if exist
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg': 'The user exists'})

        # process:create account
        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()
        # active account by email (append account data) :127.0.0.1；8000/user/active/‘id' (encode)
        serializer = Serializer(settings.SECRET_KEY)
        info = {'confirm': user.id}
        token = serializer.dumps(info)
        # send email
        subject = 'XXX Superstore welcome you'
        html_msg = '''<h1>%s, welcome you to join XXX superstore</h1>
        please click below link to active your account<br/>
        <a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>''' % (
            username, token, token)
        sender = settings.DEFAULT_FROM_EMAIL
        receiver = [email]
        send_mail(subject, '', sender, receiver, html_message=html_msg)
        # response, jump to front page
        return redirect(reverse('goods:index'))


class ActiveView(View):
    '''active account'''

    def get(self, request, token):
        # decode
        serializer = Serializer(settings.SECRET_KEY)
        try:
            # get user id
            info = serializer.loads(token)
            user_id = info['confirm']

            user = User.objects.get(id=user_id)
            user.is_active = 1
            user.save()
            return redirect(reverse('user:login'))
            # jump to sign in
        except SignatureExpired as e:
            return HttpResponse('The active link is expired')


class loginView(View):
    '''login in'''

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        '''login check'''
        # accept data
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # check data
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': 'Lack information'})

        # login check
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            # username & password correct
            if user.is_active:
                # user is active
                login(request, user)
                # jump to home
                return redirect(reverse('goods:index'))
            else:
                return render(request, 'login.html', {'errmsg': 'The account is not active'})
        else:
            return render(request, 'login.html', {'errmsg': 'Username or password is wrong'})
