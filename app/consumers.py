import json
import aiofiles
from channels.generic.websocket import AsyncWebsocketConsumer

class WalkieTalkieConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "walkie_talkie"  
        self.room_group_name = f"chat_{self.room_name}"
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"Cliente conectado en {self.room_group_name}")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print("Cliente desconectado")

    async def receive(self, text_data=None, bytes_data=None):
        if bytes_data:
            print("Recibiendo audio... reenviándolo a la sala.")
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "send_audio",
                    "audio": bytes_data
                }
            )

    async def send_audio(self, event):
        audio_data = event["audio"]
        await self.send(bytes_data=audio_data)  # Reenviar audio a todos en el grupo
