from kivy.core.window import Window

Window.size = (500, 600)
Window.minimum_width, Window.minimum_height = Window.size

import mysql.connector as mysql
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.db = mysql.connect(
            host="localhost",
            user="root",
            passwd="password",
            database="clients_all"
        )
        self.cursor = self.db.cursor()

    def validate_login(self, widget, email, pwd):
        print(email.text, pwd)

        self.cursor.execute(f"SELECT * FROM users WHERE email='{email.text}' AND password='{pwd.text}'")
        query = self.cursor.fetchall()
        if not len(query) == 1:
            widget.text = "Email e/ou senha inválidos."
        else:
            widget.text = ""
            self.manager.current = "menu"
        email.text = ""
        pwd.text = ""


class Menu(Screen):
    pass

class TestApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login_screen"))
        sm.add_widget(Menu(name="menu"))

        return sm


if __name__ == "__main__":
    TestApp().run()