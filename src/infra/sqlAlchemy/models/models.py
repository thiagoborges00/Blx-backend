
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.infra.sqlAlchemy.config.database import Base

class Produto(Base):

    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    preco = Column(Float)
    detalhamento = Column(String)
    disponivel = Column(Boolean)

    usuario_id = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"))
    usuarios = relationship("Usuario", back_populates="produtos")


class Pedido(Base):
    
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    endereco_entrega = Column(String)
    observacoes = Column(String)
    entrega = Column(Boolean, default=True)



class Usuario(Base):
   
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    telefone = Column(String)
    nome = Column(String) 
    senha = Column(String)

    produtos = relationship("Produto", back_populates="usuarios", cascade="all, delete")

