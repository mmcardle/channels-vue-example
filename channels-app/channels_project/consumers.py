from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import random
import json

COLORS = ['#4a4e4d', '#0e9aa7', '#3da4ab', '#f6cd61', '#fe8a71']


class ColorConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        maxValue = text_data_json['max']
        self.send(bytes_data=json.dumps({
            'x': random.randint(0, int(maxValue)),
            'y': random.randint(0, int(maxValue)),
            'color': random.choice(COLORS)
        }).encode('utf-8'))



class AsyncColorConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        maxValue = text_data_json['max']
        await self.send(bytes_data=json.dumps({
            'x': random.randint(0, int(maxValue)),
            'y': random.randint(0, int(maxValue)),
            'color': random.choice(COLORS)
        }).encode('utf-8'))
