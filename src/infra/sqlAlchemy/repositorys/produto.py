import pdb
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlAlchemy.models import models

class RepositorioProduto():

    def __init__(self, db:Session):
        self.db = db
    
    def criar(self, produto:schemas.Produto):
        '''pega a modelagem do produto(schema) e transforma em um objeto do modelo produto que vai pro banco '''
        #pdb.set_trace()
        db_produto = models.Produto(nome=produto.nome,
            detalhamento=produto.detalhamento,
            preco = produto.preco,
            disponivel=produto.disponivel,)
            #usuario:Usuario)
        
        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        ''' lista todos os produtos do banco '''
        produtos = self.db.query(models.Produto).all()
        return produtos