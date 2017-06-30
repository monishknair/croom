from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from app.models import ChatRoom,Archives

class Chatrooms():
  def get():
    return render(request, 'app/index.html', {})
  def post():
    return render(request, 'app', {})
  def put():
    return None
  def delete():
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
