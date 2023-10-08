from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen 
from kivymd.uix.screenmanager import MDScreenManager
from kivy.lang import Builder
from kivy.core.window import Window 
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDRectangleFlatButton 

Window.size = (360, 640)
class button_for_menu(MDRectangleFlatButton):
    font_name = '/usr/share/fonts/TTF/Dongle-Regular.ttf'
    font_size = '40sp'
    text_color = '#FFFFFF'
    line_color = [1, 1, 1, 1]

class MainScreen(MDScreen):
    def open_menu(self):
        self.ids.button1.text = 'Choose location:                  '
        menu_items=[
            {'viewclass': 'button_for_menu', 
             "text": 'Kazakhstan',
             'on_release': lambda: self.kz(), 
             'id':'first'
             },
            {'viewclass': 'button_for_menu', 
             "text": 'U.S.A.',
             'on_release': lambda: self.us(),
             },
            {'viewclass': 'button_for_menu', 
             "text": 'France',
             'on_release': lambda: self.fr(),
             },
        ]
        menu = MDDropdownMenu(
            caller=self.ids.button1,
            items=menu_items,
            width_mult=4,
            elevation=0,
            background_color = '#B1BCF5', 
            opening_time=.5,
            max_height=224,
            position='center',
        )

        menu.open()

        def kz(self):
            sm.current = 'kz_lakes'



class MyApp(MDApp):
    def build(self):
        kv = Builder.load_file('main_screen.kv')
        global sm 
        sm = MDScreenManager()
        sm.add_widget(MainScreen(name='main_screen'))

        self.menu_items = ['Item1', 'Item2', 'Item3']
        return sm




MyApp().run()
