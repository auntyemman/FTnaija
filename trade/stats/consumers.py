from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class DashboardConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('connection')
        await self.accept()
    
    async def disconnect(self, close_code):
        print(f"connection closed with code: {close_code}")
        
        return await super().disconnect(close_code) 
    
    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json["sender"]
        print(message, sender)
        
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
        
        return await super().receive(text_data, bytes_data, **kwargs)