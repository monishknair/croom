from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    max = models.IntegerField()
    access_type = models.IntegerField()

    def __unicode__(self):
        return str(self.name)

class Message(models.Model):

    msg = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    msg_type = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    owner = models.ForeignKey('app.Client', on_delete=models.CASCADE)
    room = models.ForeignKey('app.ChatRoom', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self._msg

class Client(models.Model):

    user = models.OneToOneField('auth.User')
    name = models.CharField(max_length=100)
    picture = models.FileField(null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    crooms = models.ManyToManyField('app.ChatRoom')
    active = models.BooleanField(default=True)
    picture = models.FileField()

    def __unicode__(self):
        return str(self.name)
    