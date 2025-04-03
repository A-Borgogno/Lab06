from database.DAO import DAO


class Model:
    def __init__(self):
       pass

    def fillDdYear(self):
        return DAO.getAllYear()

    def fillDdProduct(self):
        return DAO.getAllBrand()

    def fillDdRetailers(self):
        return DAO.getAllRetailers()

    def searchTop(self, anno, brand, retailer):
        return DAO.getTop(anno, brand, retailer)

    def analizza(self, anno, brand, retailer):
        return DAO.analizza(anno, brand, retailer)