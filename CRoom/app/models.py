from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ChatRoom(models.Model):

    name = models.CharField(max_length=100)
    max = models.IntegerField()

    def __unicode__(self):
        return self.name

class Archive(models.Model):

    _name = models.CharField(max_length=100)
    _size = models.CharField(max_length=100)
    _type = models.CharField(max_length=100)
    _date_added = models.DateField(auto_now_add=True)
    _owner = models.CharField(max_length=100)
    _status = models.CharField(max_length=100)

    def __unicode__(self):
        return self._name
