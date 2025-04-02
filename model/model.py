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
        return sorted(DAO.getTop(anno, brand, retailer), key=lambda v:v[1], reverse=True)

    def analizza(self, anno, brand, retailer):
        return DAO.analizza(anno, brand, retailer)