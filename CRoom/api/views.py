from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import routers
from app.models import ChatRoom, Message, User
from api.serializers import ChatRoomSerializer, MemberSerializer, MessageSerializer

class ChatRoomViewSet(viewsets.ModelViewset):
    permission_classes = []
    authentication_classes = []
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet():
    permission_classes = []
    authentication_classes = []
    def list(self, request):
        queryset = Message.objects.filter(room__in=self.request.user.usr.crooms.name)
        serializer = MessageSerializer(queryset, Many=True)
        return Response(serializer.data)

class MembersViewSet():
    permission_classes = []
    authentication_classes = []
    def list(self, request):
        queryset = Members.objects.filter(room__in=self.request.user.usr.crooms.name)
        serializer = MessageSerializer(queryset, Many=True)
        return Response(serializer.data)
