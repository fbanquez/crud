from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date,
    Sequence,
    ForeignKey,
)

from .meta import Base


# class MyModel(Base):
#     __tablename__ = 'models'
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     value = Column(Integer)


# Index('my_index', MyModel.name, unique=True, mysql_length=255)

class Departamento(Base):
    __tablename__ = 'departamentos'
    codigo = Column(Integer, Sequence('departamentos_seq'), primary_key=True)
    nombre = Column(Text, unique=True)

    def __init__(self, nombre):
        self.nombre = nombre


class Profesor(Base):
    __tablename__ = 'profesores'
    codigo   = Column(Integer, Sequence('profesores_seq'), primary_key=True)
    nombre   = Column(Text)
    fecha_nac = Column(Date)
    correo   = Column(Text)
    telefono = Column(Text)
    departamento = Column(Integer, ForeignKey('departamentos.codigo'))

    def __init__(self, nombre, fecha_nac, correo, telefono, departamento):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.correo = correo
        self.telefono = telefono
        self.departamento = departamento
