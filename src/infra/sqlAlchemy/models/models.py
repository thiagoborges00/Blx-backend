
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
    pedido_id = Column(Integer, ForeignKey("pedido.id"))
    pedido = relationship("Pedido", back_populates="produtos")

    usuario_id = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"))
    usuarios = relationship("Usuario", back_populates="produtos")

    def __repr__(self):
        return f'Produto(nome={self.nome}, id={self.id}, preco={self.preco}, detalhamento={self.detalhamento})'


class Pedido(Base):
    
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    endereco_entrega = Column(String)
    observacoes = Column(String)
    entrega = Column(Boolean, default=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id"))
    usuario = relationship("Usuario", back_populates="pedidos")

    def __repr__(self):
        return f'Pedido(id={self.id}, quantidade={self.quantidade})'



class Usuario(Base):
   
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    telefone = Column(String)
    nome = Column(String) 
    senha = Column(String)

    produtos = relationship("Produto", back_populates="usuarios", cascade="all, delete")

    def __repr__(self):
        return f'Usuario(nome={self.nome}, id={self.nome}, tel={self.telefone}, senha={self.senha})'
