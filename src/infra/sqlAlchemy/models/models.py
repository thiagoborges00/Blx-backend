
from sqlalchemy import Boolean, Column, Float, Integer, String
from src.infra.sqlAlchemy.config.database import Base

class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    detalhamento = Column(String)
    disponivel = Column(Boolean)


class Pedido(Base):
    
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    endereco_entrega = Column(String)
    observacoes = Column(String)
    entrega = Column(Boolean, default=True)



# class Usuario(Base):
#     __tablename__ = usuario
#     pass



