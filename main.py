from kivymd.app import MDApp
from kivymd.uix.widget import MDWidget
from kivy.lang.builder import Builder


Builder.load_file('data/main.kv', encoding='utf-8')


class GameLauncherWidget(MDWidget):
    pass


class GameLauncherApp(MDApp):
    def build(self):
        return GameLauncherWidget()


if __name__ == '__main__':
    GameLauncherApp().run()
