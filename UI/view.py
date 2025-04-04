import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._btnAnalizza = None
        self._btnTop = None
        self._ddRetailers = None
        self._ddProduct = None
        self._ddYear = None
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.SYSTEM
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text(self._page.title, color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        self._ddYear = ft.Dropdown(label="Anno")
        self._controller.fillDdYear()
        self._ddProduct = ft.Dropdown(label="Brand")
        self._controller.fillDdProduct()
        self._ddRetailers = ft.Dropdown(label="Retailers")
        self._controller.fillDdRetailers()
        row1 = ft.Row([self._ddYear, self._ddProduct, self._ddRetailers], alignment=ft.MainAxisAlignment.CENTER)
        
        self._btnTop = ft.ElevatedButton(text="Top vendite", on_click=self._controller.handleTop)
        self._btnAnalizza = ft.ElevatedButton(text="Analizza vendite", on_click=self._controller.handleAnalizza)
        row2 = ft.Row([self._btnTop, self._btnAnalizza], alignment=ft.MainAxisAlignment.CENTER)
        self._page.add(row1, row2)

        # button for the "hello" reply

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
