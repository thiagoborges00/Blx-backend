from  fastapi import Depends, FastAPI
from src.infra.sqlAlchemy.config.database import create_db, get_db
from src.infra.sqlAlchemy.repositorys.produto import RepositorioProduto
from src.schemas.schemas import Produto
from sqlalchemy.orm import Session

create_db()
app = FastAPI()


@app.post('/produtos')
def cadastrar_produto(produto:Produto, db:Session = Depends(get_db)):
    '''para cadastrar o produto a funcao recebe a sessao do banco 
    e o produto em si, e retorna o produto cadastrado'''

    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos')
def listar_produtos(db:Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos
