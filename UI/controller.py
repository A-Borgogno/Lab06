import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._retailer = None
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDdYear(self):
        date = self._model.fillDdYear()
        self._view._ddYear.options.append(ft.dropdown.Option("Nessun filtro"))
        for d in date:
            self._view._ddYear.options.append(ft.dropdown.Option(d))
        self._view.update_page()

    def fillDdProduct(self):
        self._view._ddProduct.options.append(ft.dropdown.Option("Nessun filtro"))
        for p in self._model.fillDdProduct():
            self._view._ddProduct.options.append(ft.dropdown.Option(p))
        self._view.update_page()

    def fillDdRetailers(self):
        self._view._ddRetailers.options.append(ft.dropdown.Option("Nessun filtro", on_click=self.readRetailer))
        for r in self._model.fillDdRetailers():
            self._view._ddRetailers.options.append(ft.dropdown.Option(data=r, text=r, on_click=self.readRetailer))
        self._view.update_page()

    def handleTop(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Caricamento in corso", size=19, weight=ft.FontWeight.BOLD))
        self._view.update_page()
        anno = self._view._ddYear.value
        brand = self._view._ddProduct.value
        retailer = self._retailer
        if retailer is None:
            top = self._model.searchTop(anno, brand, retailer)
        else:
            top = self._model.searchTop(anno, brand, retailer.codice)
        self._view.txt_result.controls.clear()
        if len(top) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita trovata con i filtri impostati", size=20))
            self._view.update_page()
            return
        for i in range(0, min(5, len(top))):
            self._view.txt_result.controls.append(ft.Text(f"Data: {top[i][3]} Retailer: {top[i][0]} Brand: {top[i][2]} Ricavo: {top[i][1]}"))
        self._view.update_page()

    def handleAnalizza(self, e):
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Caricamento in corso", size=19, weight=ft.FontWeight.BOLD))
        self._view.update_page()
        anno = self._view._ddYear.value
        brand = self._view._ddProduct.value
        retailer = self._retailer
        if retailer is None:
            dati = self._model.analizza(anno, brand, retailer)
        else:
            dati = self._model.analizza(anno, brand, retailer.codice)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {dati[0][0]}"
                                                      f"\nNumero vendite: {dati[0][1]}"
                                                      f"\nNumero retailers coinvolti: {dati[0][2]}"
                                                      f"\nNumero prodotti coinvolti: {dati[0][3]}"))
        self._view.update_page()

    def readRetailer(self, e):
        self._retailer = e.control.data
