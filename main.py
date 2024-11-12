from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.card import MDCard

data = {
    "Expenses": [
        {"amount": 34, "category": "Grocery"},
        {"amount": 120, "category": "Transport"},
    ],
    "Income": [
        {"amount": 500, "category": "Salary"},
        {"amount": 150, "category": "Freelance"},
    ],
}


class Tab(BoxLayout, MDTabsBase):
    """Class implementing content for each tab."""
    title = StringProperty("")


class FirstApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"

        self.menu_items = [
            {"viewclass": "OneLineListItem", "text": "Home", "on_release": lambda x="home": self.menu_callback(x)},
            {"viewclass": "OneLineListItem", "text": "Modify", "on_release": lambda x="modify": self.menu_callback(x)},
            {"viewclass": "OneLineListItem", "text": "Settings", "on_release": lambda x="settings": self.menu_callback(x)},
        ]

        self.menu = MDDropdownMenu(
            items=self.menu_items,
            width_mult=4,
        )
        return Builder.load_file('first.kv')

    def open_menu(self, instance):
        self.menu.caller = instance
        self.menu.open()

    def menu_callback(self, screen_name):
        # print(f"Nom Ecran: {screen_name}")
        self.root.current = screen_name
        self.menu.dismiss()

    # def change_screen(self, screen_name):
    #     self.root.current = screen_name

    def account_callback(self):
        print('c')

    def on_start(self):
        self.load_cards("Expenses")
        self.load_cards("Income")

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        """Called when switching tabs."""
        if tab_text in data:
            self.clear_cards(tab_text)
            self.load_cards(tab_text)

    def clear_cards(self, category):
        if category == "Expenses":
            card_container = self.root.ids.expenses_container
        elif category == "Income":
            card_container = self.root.ids.income_container
        else:
            return

        card_container.clear_widgets()
        card_container.height = 0

    def load_cards(self, category):
        if category == "Expenses":
            card_container = self.root.ids.expenses_container
        elif category == "Income":
            card_container = self.root.ids.income_container
        else:
            return

        card_container.clear_widgets()

        card_container.height = 0

        screen_width = self.root.width

        for item in data[category]:
            card = MDCard(
                style="outlined",
                md_bg_color="whitesmoke",
                line_color="grey",
                pos_hint={"center_x": 0.5},
                size_hint=(0.85, None),
                height="100dp",
                padding="10dp"
            )

            card.add_widget(self.create_label(f"Category: {item['category']}", "H6"))
            card.add_widget(self.create_label(f"Amount: ${item['amount']}", "H6"))

            card_container.add_widget(card)
            card_container.height += card.height

    def create_label(self, text, style):
        from kivymd.uix.label import MDLabel
        return MDLabel(
            text=text,
            font_style=style,
            halign="left",
            theme_text_color="Secondary",
            adaptive_height=True,
        )


if __name__ == '__main__':
    FirstApp().run()
