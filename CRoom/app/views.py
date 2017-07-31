from app.forms import UserLoginForm, UserRegForm
from app.models import Archives, ChatRoom, Client, Message
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.db import transaction
from django.contrib.auth.models import User

class UserLogin(View):
    def get(self, request):
        return render(request, 'app/Login.html', {'Type': 'Get-Login'})

    def post(self, request):
        form = UserLoginForm(self.request.POST or None)
        if form.is_valid():
            username = form.validated_data.get('username')
            password = form.validated_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
        return render(request, 'app/login.html', {'Type': 'Post-Login', 'form': form})


class UserLogout(View):
    def get(self, request):
        logout(request)
        return render(request, 'app/login.html', {'Type': 'Logout'})

class UserReg(View):
    def get(self, request):
        return render(request, 'app/reg.html', {'Type': 'get'})

    def post(self, request):
        form = UserRegForm(self.request.POST or None)
        if form.is_valid():
            username = form.validated_data.get('username')
            password = form.validated_data.get('password')
            email = form.validated_data('email')
            name = form.validated_data('name')
            picture = form.validated_data('picture')
            with transaction.atomic():
                usr=User.objects.create_user(username=username, password=password)
                Client.objects.create(name=name,
                                      picture=picture,
                                      user=usr)

                return render(request, 'app/reg.html', {'Type':'post', 'status':'successful'})
        return render(request, 'app/reg.html', {'Type':'get', 'status':'reg_failed', 'errors':form.error})

class Profile(View):
    def get(self, request):
        data={}
        return render(request, 'app/Profile.html', {'data':data})

    def put(self, request):
        #update profile fields.
        return render(request, 'app/Profile.html', {})

    def delete(self, request):
        #delete user.
        return render(request, 'app/Profile.html', {})

class Chatrooms(View):
    def get(self, request):
        return render(request, 'app/index.html', {})

    def post(self, request):
        return render(request, 'app/index.html', {})
    
    def put(self, request):
        return render(request, 'app/index.html', {})

    def delete(self, request):
        return render(request, 'app/index.html', {})

class Members(View):
    def get(self, request):
        return render(request, 'app/index.html', {})

    def post(self, request):
        return render(request, 'app/members.html',{})

    def put(self, request):
        return render(request, 'app/members.html',{})

    def delete(self, request):
        return render(request, 'app/members.html',{})

class Working(View):
    def get(self, request):
        return(request, 'app/chatroom.html', {'user':user})
    def post(self, request):
        return(request, 'app/chatroom.html', {'user':user})