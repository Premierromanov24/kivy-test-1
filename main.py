from os import name
from typing import Text
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

"""
import socket

HEADER = 64
PORT = 5055
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.29.204.216"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

"""



class MyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):
    name = ObjectProperty(None)
    oclass = ObjectProperty(None)
    date = ObjectProperty(None)
    def button1pressed(self):
        return 1
        """
        if str(self.name.text) == DISCONNECT_MESSAGE:
            send(DISCONNECT_MESSAGE)
        send(str(self.name.text))"""
    pass

        


if __name__ == "__main__":
    MyApp().run()
