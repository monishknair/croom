from app.forms import UserLoginForm, UserRegForm
from app.models import Archives, ChatRoom
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.db import transaction

class UserLogin():
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


class UserLogout():
    def get(self, request):
        logout(request)
        return render(request, 'app/login.html', {'Type': 'Logout'})

class UserReg():
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
                Client.objects.create(name=,
                                      picture=,
                                      user=usr)

                return render(request, 'app/reg.html', {'Type':'post', 'status':'successful'})
        return render(request, 'app/reg.html', {'Type':'get', 'status':'reg_failed', 'errors':form.error})

class Profile():
    def get(self, request):
        data={}
        return render(request, 'app/Profile.html', {'data':data})

    def post(self, request):
        return render(request, 'app/Profile.html', {})

    def put(self, request):
        return render(request, 'app/Profile.html', {})

    def delete(self, request):
        return render(request, 'app/Profile.html', {})

class Chatrooms():
    def get(self, request):
        return render(request, 'app/index.html', {})

    def post(self, request):
        return render(request, 'app', {})

    def put(self, request):
        return None

    def delete(self, request):
        return None

class Members():
    def get(self, request):
        return render(request, 'app/index.html', {})

    def post(self, request):
      return render(request, 'app', {})

    def put(self, request):
        return None

class Messages():
    def get(self, request):
      return render(request, 'app/index.html', {})

    def post(self, request):
        return render(request, 'app', {})

    def put(self, request):
        return None

    def delete(self, request):
      return None
