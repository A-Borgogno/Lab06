from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():

    @staticmethod
    def getAllYear():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select distinct Year(Date) from go_daily_sales"
        cursor.execute(query)
        listaDate = []
        for row in cursor.fetchall():
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

    @staticmethod
    def getAllRetailers():
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


    @staticmethod
    def getTop(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select gds.Retailer_code, gds.Quantity, gds.Unit_sale_price, gp.Product_brand, gds.Date from go_daily_sales gds, go_products gp where gds.Product_number = gp.Product_number"
        if anno != "Nessun filtro" and anno is not None:
            query += f" and Year(Date) = {anno}"
        if brand != "Nessun filtro" and brand is not None:
            query += f" and gp.Product_brand = '{brand}'"
        if retailer != "Nessun filtro" and retailer is not None:
            query += f" and Retailer_code = {retailer}"
        query += f" order by gds.Quantity*gds.Unit_sale_price desc limit 5"
        cursor.execute(query)
        listaTop = []
        for row in cursor.fetchall():
            listaTop.append((row[0], row[1]*row[2], row[3], row[4]))
        cursor.close()
        cnx.close()
        return listaTop

    @staticmethod
    def analizza(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        query = "select sum(gds.Quantity*gds.Unit_sale_price), count(*), count(distinct(gds.Retailer_code)), count(distinct (gp.Product)) from go_daily_sales gds, go_products gp where gds.Product_number = gp.Product_number"
        if anno != "Nessun filtro" and anno is not None:
            query += f" and Year(Date) = {anno}"
        if brand != "Nessun filtro" and brand is not None:
            query += f" and gp.Product_brand = '{brand}'"
        if retailer != "Nessun filtro" and retailer is not None:
            query += f" and Retailer_code = {retailer}"
        cursor.execute(query)
        listaDati = []
        for row in cursor.fetchall():
            listaDati.append((row[0], row[1], row[2], row[3]))
        cursor.close()
        cnx.close()
        return listaDati