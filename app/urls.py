from django.urls import path
from app import consumers  # Importa tus WebSocket Consumers

websocket_urlpatterns = [
    path("ws/walkie-talkie/", consumers.WalkieTalkieConsumer.as_asgi()),
]
