from sqlalchemy.orm import Session
from src.schemas.schemas import Pedido
from src.infra.sqlAlchemy.models.models import Pedido


class RepositorioPedido():

    def __init__(self, db:Session):
        self.db = db

    def cadastrar(self, pedido:Pedido):
        '''cadastra um pedido '''

        pedido_feito = Pedido(
            endereco_entrega=pedido.endereco_entrega,
            entrega=pedido.entrega,
            observacoes=pedido.observacoes,
            quantidade=pedido.quantidade
        )
        self.db.add(pedido_feito)
        self.db.commit()
        self.db.refresh(pedido_feito)
        return pedido_feito

    

    def listar(self):
        pedidos = self.db.query(Pedido).all()
        return pedidos
    

    def pesquisar(self, id:int):
        # try:
        #     pedido = self.db.get(Pedido, id)
        #     return pedido
        # except:
        #     return "erro"
        pedido = self.db.get(Pedido, id)
        return pedido

    def remover(self, id:int):
        pedido = self.pesquisar(id)
        self.db.delete(pedido)
        self.db.commit()
        return "excluido"

    
