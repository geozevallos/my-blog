from flask_restful import Resource
from flask_mysqldb import MySQL


class CategoriaApi(Resource):
    def get(self):
        
        # cur = mysql.connection.cursor()

        return "categoria"

        