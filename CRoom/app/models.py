from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    max = models.IntegerField()
    access_type = models.IntegerField()

    def __unicode__(self):
        return self.name

class Message(models.Model):

    msg = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    msg_type = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    owner = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return self._msg

class User(models.Model):

    name = models.CharField(max_length=100)
    picture = models.FileField(null=True, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    crooms = models.name = models.ForeignKey('app.ChatRoom', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    def __unicode__(self):
        return self.name
