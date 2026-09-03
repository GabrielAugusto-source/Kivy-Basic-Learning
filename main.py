from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image, AsyncImage

class MainApp(App):
    def build(self):
        
        img = AsyncImage(
            
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': .5, 'center_y': .5}
            
        )
        return Image(source="images/arthur.png")

if __name__ == "__main__":
    MainApp().run()
