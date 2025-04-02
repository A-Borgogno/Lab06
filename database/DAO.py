from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getAllYear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select Year(Date) from go_daily_sales"
        cursor.execute(query)
        listaDate = []
        for row in cursor.fetchall():
            if row[0] not in listaDate:
                listaDate.append(row[0])
        cursor.close()
        cnx.close()
        return listaDate

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select Product_brand from go_products"
        cursor.execute(query)
        listaProdotti = []
        for row in cursor.fetchall():
            if row[0] not in listaProdotti:
                listaProdotti.append(row[0])
        cursor.close()
        cnx.close()
        return listaProdotti

    def getAllRetailers(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select * from go_retailers"
        cursor.execute(query)
        listaRetailers = []
        for row in cursor.fetchall():
            if row[0] not in listaRetailers:
                listaRetailers.append(Retailer(row[0], row[1], row[2], row[3]))
        cursor.close()
        cnx.close()
        return listaRetailers

    def getTop(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select * from go_daily_sales gds, go_products gp where gds.Product_number = gp.Product_number"
        if anno != "Nessun filtro":
            query += f" and Year(Date) = {anno}"
        if brand != "Nessun filtro":
            query += f" and Product_brand = {brand}"
        if retailer != "Nessun filtro":
            query += f" and Retailer_code = {retailer}"
        cursor.execute(query)
        listaTop = []
        for row in cursor.fetchall():
            listaTop.append(row[0])
            listaTop.__hash__()
        cursor.close()
        cnx.close()
        return listaTop