from django.contrib.auth.models import User, Group
from rest_framework import serializers
from app.models import ChatRoom, Message, User

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

class  MessageSerializer(serializers.Serializer):
    msg = serializers.CharField(max_length=1000, required=False)

class MessageDetailsSerializes(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'