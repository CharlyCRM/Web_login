from flask import Flask, render_template, request, redirect, url_for
import db
from models import Usuario # Importo la clase Usuario para poder crear la tabla
from db import session

app = Flask(__name__) # Creamos el servidor de Flask


# Damos acceso mediante POST para acceder al formulario con los datos de username y passwolrd
# Damos acceso emdiante GET para acceder al formulario por primera vez
@app.route('/')
def home():
    return render_template("index.html")

# Valida si el usuario y contraseña existe en la base da datos
@app.route('/validar_usuario', methods=['POST'])
def validar_usuario():
    username = request.form['username']
    password = request.form['password']

    user = session.query(Usuario).filter_by(username=username, password=password).first()

    if user:
        # Los datos de inicio de sesión son válidos, redirige a la web administrador
        return "Usuario encontrado en la Base de Datos"  
    else:
        
        return "Usuario no existe en la base de Datos"


if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    app.run(debug=True) # Ejecutamos el servidor
