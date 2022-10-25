import pdb
from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import Depends, FastAPI, status
from src.infra.sqlAlchemy.repositorys.pedido import RepositorioPedido
from src.infra.sqlAlchemy.config.database import create_db, get_db
from src.infra.sqlAlchemy.repositorys.produto import RepositorioProduto
from src.infra.sqlAlchemy.repositorys.usuario import RepositorioUsuario
from src.schemas.schemas import Usuario, UsuarioSimples, Produto, Pedido
from sqlalchemy.orm import Session

#create_db()
app = FastAPI()

#PRODUTOS
@app.post('/produtos',tags=["Produtos"], status_code=status.HTTP_201_CREATED,
# responses={
#     201:{
#         "description":"Produto cadastrado com sucesso",
#         "content":{
#             "application/json":{
#                 "example":{
#                     "nome":"pizza",
#                     "detalhamento":"sabor carne de sol com banana tamanho GG",
#                     "preco":63.50,
#                     "disponivel":True,
#                     "usuario_id":2
#                 }
#             }
#         }
#     }
# }
)
def cadastrar_produto(produto:Produto, db:Session = Depends(get_db)):
    '''para cadastrar o produto a funcao recebe a sessao do banco 
    e o produto em si, e retorna o produto cadastrado'''

    produto_criado = RepositorioProduto(db).criar(produto)
    if produto_criado is None: 
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"detail":"produto já cadastrado"})
    return produto_criado


@app.get('/produtos', tags=["Produtos"], response_model=List[Produto], )
def listar_produtos(db:Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@app.delete('/produtos/{id}', tags=["Produtos"], responses={
    # 200:{
    #     "description":"remoção com sucesso",
    #     "content":{
    #         "application/json":{
    #             "example":"xxxxx"
    #         }
    #     }
    # },
    404:{
        "description":"produto não encontrado",
    },
    # 422:{
    #     "description":"erro de validação nos parametros"
    # },
    },
    summary ="Deletar Produtos", response_model=Produto)
def remover_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).remove(id)
    if produto is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(produto))
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"Produto não encontrado"})


@app.get('/produtos/{id}', tags=["Produtos"])
def pesquisar_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).pesquisar(id)
    if produto is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"produto naão encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(produto))


@app.put('/produtos/{id}', tags=["Produtos"])
def atualizar_produto(produto:Produto, id:int, db:Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(db).atualizar(id=id,produto=produto)
    if produto_atualizado is None: 
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"produto não encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail":"produto atualizado"})



#PEDIDOS
@app.get('/pedidos', tags=["Pedidos"])
def listar_pedidos(db:Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos


@app.post('/pedidos', tags=["Pedidos"])
def cadastrar_pedido(pedido:Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).cadastrar(pedido)
    return pedido


#USUARIOS
@app.get('/usuarios', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@app.post('/usuarios', tags=["Usuarios"], status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar_usuario(user:Usuario, db:Session = Depends(get_db)):
    novo_usuario = RepositorioUsuario(db).criar(user)
    return novo_usuario


@app.delete('/usuarios/{id}', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=UsuarioSimples)
def remover_usuario(id:int, db:Session = Depends(get_db)):
    deletado = RepositorioUsuario(db).remover(id)
    return deletado


@app.get('/usuarios/{id}', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=Usuario)
def pesquisar_usuario(id:int, db:Session = Depends(get_db)):
    pdb.set_trace()
    usuario = RepositorioUsuario(db).pesquisar(id)
    if not usuario : return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"usuário não encontrado"})
    return usuario
