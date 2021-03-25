import db 
from sqlalchemy import  Column, String, Integer

class Tarea(db.Base):
    __tablename__ = 'tareas'

    id = Column(Integer, primary_key=True)
    titulo= Column(String(100))
    descripcion= Column(String(250))
    estado= Column(String(100))
    responsable= Column(String(200))
    fecha= Column(String(100))

    def __init__(self, titulo, descripcion, estado, responsable, fecha):
        self.titulo = titulo
        self.descripcion = descripcion 
        self.estado = estado
        self.responsable = responsable
        self.fecha = fecha 


    def __repr__ (self):
        return f'{self.id}, {self.titulo}, {self.descripcion}, {self.estado}, {self.responsable},{self.fecha}'

    def __str__(self):
        return f'{self.id}, {self.titulo}, {self.descripcion}, {self.estado}, {self.responsable},{self.fecha}'

db.Base.metadata.create_all(db.engine)

class Estado(db.Base):
    __tablename__ = 'estados'

    id = Column(Integer, primary_key=True)
    nombreEstado= Column(String(100))
    descripcion= Column(String(250))

    def __init__(self, nombreEstado, descripcion):
        self.nombreEstado = nombreEstado
        self.descripcion = descripcion 
        

    def __repr__ (self):
        return f'{self.id},{self.nombreEstado},{self.descripcion}'

    def __str__(self):
        return self.nombre

db.Base.metadata.create_all(db.engine)

class Usuario(db.Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,primary_key=True)
    nombre = Column(String(100))
    apellido = Column(String(250))
    email = Column(String(65))


    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
    
    def __repr__ (self):
        return f'{self.id},{self.nombre},{self.apellido},{self.email}'

    def __str__(self):
        return f'{self.id},{self.nombre},{self.apellido},{self.email}'


db.Base.metadata.create_all(db.engine)

