from sqlalchemy.orm import Session
from sqlalchemy import update
from src.schemas import schemas
from src.infra.sqlAlchemy.models import models

class RepositorioProduto():

    def __init__(self, db:Session):
        self.db = db
    
    def criar(self, produto:schemas.Produto):
        '''pega a modelagem do produto(schema) e transforma em um objeto do modelo produto que vai pro banco '''
        #if self.pesquisar(produto.id): return None
        db_produto = models.Produto(nome=produto.nome,
            detalhamento=produto.detalhamento,
            preco = produto.preco,
            disponivel=produto.disponivel,
            usuario_id=produto.usuario_id)
            #usuario:Usuario)
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        ''' lista todos os produtos do banco '''
        produtos = self.db.query(models.Produto).all()
        return produtos
    

    def pesquisar(self, id:int):
        produto = self.db.get(models.Produto, id)
        return produto if produto != None else None


    def remove(self, id:int):
        '''remove o produto com o id passado por parametro'''
        produto = self.db.get(models.Produto,id)
        if produto is not None :
            self.db.delete(produto)
            self.db.commit()
        return produto


    def atualizar(self, id:int, produto:schemas.Produto):
        '''atualiza um produto atravez de um produto enviado por parametro'''
        existe = self.pesquisar(id)
        if existe:
            update_stmt = update(models.Produto).where(models.Produto.id == id).values(
                nome=produto.nome,
                detalhamento=produto.detalhamento,
                preco = produto.preco,
                disponivel=produto.disponivel,
            )
            self.db.execute(update_stmt)
            self.db.commit()
            return True
        return existe
