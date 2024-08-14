#Llamar libreria de flask
from flask import Flask

#Invitar cual va aser el archivo principal a ejecutar
#App -> recicbir informacion de flask
app=Flask(__name__)

#Rutas
@app.route('/')

#Crear una funcon paa verificar si funciona la app
def home():
    return "Hola mundo esto esta funcionando"

#Iniciar la pagina principal
if __name__=='__main__': 
    app.run()