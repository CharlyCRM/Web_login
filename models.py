from sqlalchemy import  Column, Integer, String
import db

class Usuario(db.Base):
    '''Clase Usuario -> Contiene los atributos para realizar los logins
        ArgP:
        username: Nombre del usuario
        password: Contraseña del usuario'''
    __tablename__ = "usuarios"
    __table_args__ = {'sqlite_autoincrement': True}
    id_usuario = Column(Integer, primary_key=True)
    username = Column(String(100))
    password = Column(String(10))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'''
                Usuario: {self.username}
                Contraseña: {self.password}'''