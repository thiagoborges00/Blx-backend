from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, FastAPI, status
from src.infra.sqlAlchemy.repositorys.pedido import RepositorioPedido
from src.infra.sqlAlchemy.config.database import create_db, get_db
from src.infra.sqlAlchemy.repositorys.produto import RepositorioProduto
from src.schemas.schemas import Pedido, Produto
from sqlalchemy.orm import Session

create_db()
app = FastAPI()

#PRODUTOS
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
    200:{
        "description":"remoção com sucesso",
    },
    404:{
        "description":"produto não encontrado",
    },
    422:{
        "description":"erro de validação(url ou parametros)"
    },},
    summary ="Deletar Produtos",)
def remover_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).remove(id)
    if produto["detail"] == f'cliente  de id {id} removido com sucesso':
        return JSONResponse(status_code=status.HTTP_200_OK, content=produto)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=produto)

@app.get('/produtos/{id}')
def pesquisar_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).pesquisar(id)
    if produto["detail"] == 'produto naão encontrado':
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=produto)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(produto))

#PEDIDOS
@app.get('/pedidos')
def listar_pedidos(db:Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos

@app.post('/pedidos')
def cadastrar_pedido(pedido:Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).cadastrar(pedido)
    return pedido
