# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        btn1 = Button(text="hello")
        self.add_widget(btn1)

        btn2 = Button(text="hello")
        self.add_widget(btn2)

        btn3 = Button(text="hello")
        self.add_widget(btn3)

        btn4 = Button(text="hello")
        self.add_widget(btn4)

        btn5 = Button(text="hello")
        self.add_widget(btn5)

        btn6 = Button(text="hello")
        self.add_widget(btn6)

        btn7 = Button(text="hello")
        self.add_widget(btn7)

        btn8 = Button(text="hello")
        self.add_widget(btn8)

        btn9 = Button(text="hello")
        self.add_widget(btn9)

        btn10 = Button(text="hello")
        self.add_widget(btn10)



class MainApp(App):
    def build(self):
        MS = MainScreen()
        return MS

if __name__=="__main__":
    MainApp().run()