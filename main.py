from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen


class Tab(Screen, MDTabsBase):
    """A class that represents a custom tab in MDTabs."""
    pass


class FirstApp(MDApp):
    def build(self):
        return Builder.load_file('first.kv')

    def on_tab_switch(self, tab_text):
        print(f"Switched to tab: {tab_text}")

    def callback(self):
        print("Menu button pressed!")

    def account_callback(self):
        print("Account button pressed!")



# Running the app
FirstApp().run()
