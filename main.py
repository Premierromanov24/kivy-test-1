from os import name
from typing import Text
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class MyApp(App):
    def build(self):
        return MyGrid()

class MyGrid(Widget):
    name = ObjectProperty(None)
    oclass = ObjectProperty(None)
    date = ObjectProperty(None)
    def button1pressed(self):
        print(self.name.text, self.oclass.text, self.date.text)
    pass

        


if __name__ == "__main__":
    MyApp().run()
