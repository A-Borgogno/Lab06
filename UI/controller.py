import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
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
        self._view._ddRetailers.options.append(ft.dropdown.Option("Nessun filtro"))
        for r in self._model.fillDdRetailers():
            self._view._ddRetailers.options.append(ft.dropdown.Option(data=r, text=r))
        self._view.update_page()

    def handleTop(self):
        anno = self._view._ddYear.value
        brand = self._view._ddProduct.value
        retailer = self._view._ddRetailers.data
        # if anno=="Nessun filtro" and brand=="Nessun filtro" and retailer=="Nessun filtro":
        #     self._model.getBest()
        #     # aggiorna il listView
        # elif anno=="Nessun filtro" and brand=="Nessun filtro":
        #     self._model.getBestRetailer()
        #     # aggiorna il listView
        # elif brand=="Nessun filtro" and retailer=="Nessun filtro":
        #     self._model.getBestAnno()
        #     #aggiorna il listView
        # elif anno=="Nessun filtro" and retailer=="Nessun filtro":
        #     self._model.getBestBrand()
        top = self._model.searchTop(anno, brand, retailer)
        print(top)