from tkinter.font import names

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.utils import platform
from kivy.core.window import Window
from kivy.clock import Clock

Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
if platform == "android":
    Window.softinput_mode = "below_targets"


class Ui(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        # Carga estilos globales
        Builder.load_file('design.kv')

        # Crea el gestor de pantallas
        self.sm = Ui()

        # Carga las pantallas de manera diferida
        Clock.schedule_once(self.load_screens, 0)

        return self.sm

    def load_screens(self, *args):
        # Importar pantallas
        from screens.home_screen import HomeScreen
        from screens.main_screen import MainScreen
        from screens.historia_camiri import HistoriaCamiriScreen

        # Cargar archivos .kv asociados
        Builder.load_file('home_screen.kv')
        Builder.load_file('main_screen.kv')
        Builder.load_file('historia_camiri.kv')

        # Añadir pantallas
        self.sm.add_widget(HomeScreen(name='home'))
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(HistoriaCamiriScreen(name='historia_camiri'))

        # Mostrar la primera pantalla
        self.sm.current = 'home'


if __name__ == '__main__':
    MainApp().run()
