from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import routers
from app.models import ChatRoom, Message, Client
from api.serializers import ChatRoomSerializer, MemberSerializer, MessageSerializer

class ChatRoomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    authentication_classes = []
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

class MessageViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]
    authentication_classes = []
    queryset = Message.objects.all()
    def list(self, request):
        queryset = Message.objects.filter(room__in=self.request.user.usr.crooms)
        serializer = MessageSerializer(queryset, Many=True)
        return Response(serializer.data)

class MembersViewSet(viewsets.ViewSet):
    permission_classes = [IsAdmin]
    authentication_classes = []
    queryset = Client.objects.all()
    def list(self, request):
        queryset = Client.objects.filter(room__in=self.request.user.usr.crooms)
        serializer = MessageSerializer(queryset, Many=True)
        return Response(serializer.data)
