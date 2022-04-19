from os import name
from typing import Text
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.utils import platform
from kivy.properties import StringProperty
from plyer import gps


import socket

HEADER = 64
PORT = 5055
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.29.204.216"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg) -> str:
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(2048).decode(FORMAT)




class MyApp(App):
    
    
    def build(self):
        
        return MyGrid()

class MyGrid(Widget):
    name = ObjectProperty(None)
    oclass = ObjectProperty(None)
    date = ObjectProperty(None)  
    
    Gps_configured = False

    def request_android_permission(self):
        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        request_permissions([Permission.ACCESS_COARSE_LOCATION,
                             Permission.ACCESS_FINE_LOCATION], callback)

    def on_location(self, **kwargs):
        self.gps_location = '\n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])

    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)

    def button1pressed(self):
        if not self.Gps_configured:
            
            try:
                gps.configure(on_location=self.on_location,
                                on_status=self.on_status)
                gps.start()
                self.Gps_configured = True
            except NotImplementedError:
                send("GPS not implemented")
            
            if platform == "android":
                self.request_android_permissions()
            else:
                send("Platform is not android")
        
        self.oclass.text = ""
        if str(self.name.text) == DISCONNECT_MESSAGE:
            send(DISCONNECT_MESSAGE)
        self.date.text = send(str(self.name.text))
        if self.Gps_configured:
            send(str(self.gps_location))
        else:
            send("Gps is not configured")
    pass

        


if __name__ == "__main__":
    MyApp().run()
