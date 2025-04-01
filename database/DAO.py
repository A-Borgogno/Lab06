from database.DB_connect import DBConnect


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

        return listaDate
