# from api.categoria_api import CategoriaApi
# from api.hello_api import Helloworld
from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource, Api




#Inicializa con varios parámetros
app = Flask(__name__)
mysql = MySQL(app)
api = Api(app)

#Seter parametros
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "myblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"




@app.route('/')
def index():
    # cur = mysql.connection.cursor()
    return "Hello :) "



class CategoriaPostApi(Resource):
    def get(self, id):
        cur = mysql.connection.cursor()
        cur.execute('''SELECT p.titulo, c.nombre FROM myblog.post as p
                        LEFT JOIN myblog.categoria as c
                        ON p.idcategoria = c.idcategoria
                        WHERE p.idcategoria = ''' + id )
        result = cur.fetchall()
        return str(result)

class CategoriaApi(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM  categoria")
        result = cur.fetchall()
        return str(result)


class PostsApi(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM  post")
        result = cur.fetchall()
        return str(result)




# Redirige a una clase
# api.add_resource(Helloworld, '/hello')

#A categorias
api.add_resource(CategoriaApi, '/categoria')


api.add_resource(PostsApi, '/posts')


api.add_resource(CategoriaPostApi, '/categoria/<id>/posts')