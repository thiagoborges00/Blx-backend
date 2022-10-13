from fastapi.responses import JSONResponse
from fastapi import Depends, FastAPI, status
from src.infra.sqlAlchemy.repositorys.pedido import RepositorioPedido
from src.infra.sqlAlchemy.config.database import create_db, get_db
from src.infra.sqlAlchemy.repositorys.produto import RepositorioProduto
from src.schemas.schemas import Pedido, Produto
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

@app.delete('/produtos/{id}', responses={
   
})
def remover_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).remove(id)
    if produto == 'excluido':
        return JSONResponse(status_code=status.HTTP_200_OK, content=produto)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=produto)

@app.get('/pedidos')
def listar_pedidos(db:Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos

@app.post('/pedidos')
def cadastrar_pedido(pedido:Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).cadastrar(pedido)
    return pedido
