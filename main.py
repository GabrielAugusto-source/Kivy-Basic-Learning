import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


red = (1, 0, 0, 1)
green = (0, 1, 0, 1)
blue = (0, 0, 1, 1)
yellow = (1, 1, 0, 1)


class HBoxLayoutExample(App):
    def build(self):
        self.title = "Kivy Colors"
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        colors = [red, green, blue, yellow]

        for i in range(5):
            btn = Button(text=f"Este é o botão #{i + 1}", background_color=random.choice(colors))
            layout.add_widget(btn)

        return layout

if __name__ == "__main__":
        app = HBoxLayoutExample()
        app.run()
        


