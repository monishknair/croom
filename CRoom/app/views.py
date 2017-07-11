from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import (
                                  authenticate,
                                  get_user_model,
                                  login,
                                  logout,
                                )
from app.models import ChatRoom,Archives
from app. forms import UserLoginForm,UserRegForm

class UserLogin():
  def get(self, request):
    return render(request, 'app/Login.html', {'Type':'Get-Login'})
  def post(self, request):
    form = UserLoginForm(self.request.POST or None)
    if form.is_valid():
      username = form.validated_data.get('username')
      password = form.validated_data.get('password')
      user = authenticate(username=username, password=password)
      login(request, user)
    return render(request, 'app/login.html', {'Type':'Post-Login','form':form})  

class UserLogout():
  def get(self, request):
    logout(request)
    return render(request, 'app/login.html',{'Type':'Logout'})

class UserReg():
  def get(self, request):
    return render(request, 'app/reg.html',{'Type':'get'})
  def post(self, request):
    return render(request, 'app/reg.html',{'Type':'post'})    

class Profile():
  def get(self ,request):
    return render(request, 'app/Profile.html',{})
  def post(self, request):
    return render(request, 'app/Profile.html',{})
  def put(self, request):
    return render(request, 'app/Profile.html',{})
  def delete(self, request):
    return render(request, 'app/Profile.html',{})

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
  def get():
    return render(request, 'app/index.html', {})
  def post():
    return render(request, 'app', {})
  def put():
    return None

class Messages():
  def get():
    return render(request, 'app/index.html', {})
  def post():
    return render(request, 'app', {})
  def put():
    return None
  def delete():
    return None
