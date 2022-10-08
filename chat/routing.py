from re import I
from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path('ws/sc/', consumer.MySyncConsumer.as_asgi())
]