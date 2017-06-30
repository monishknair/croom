from django.conf.urls import patterns, url
from rest_framework import routers
from api.views import MembersViewSet, MessageViewSet, ChatRoomViewSet

router = routers.SimpleRouter()
router.register(r'chatrooms', ChatRoomViewSet)
router.register(r'message', MessageViewSet)
router.register(r'members', MembersViewSet)

urlpatterns = router.urls
