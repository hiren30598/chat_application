import json

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class MySyncConsumer(WebsocketConsumer):

    def websocket_connect(self, event):
        print('Websocket connected...', event)
        print(self.channel_name)
        self.room = "testing"
        async_to_sync(self.channel_layer.group_add)(
            self.room,
            self.channel_name
        )
        self.accept()

    def websocket_receive(self, event):
        print('Websocket Received...', event)
        print(event.get('text'))
        async_to_sync(self.channel_layer.group_send)(
                self.room,
                {
                    'type': 'message_received',
                    'message': event.get('text')
                }
        )

    def websocket_disconnect(self, event):
        print('Websocket disonnected', event)
        raise StopConsumer

    def message_received(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
                'message': message
        }))