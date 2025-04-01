from database.DAO import DAO


class Model:
    def __init__(self):
       pass

    def fillDdYear(self):
        return DAO.getAllYear()