from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.sqlAlchemy.config.database import get_db
from src.infra.sqlAlchemy.repositorys.produto import RepositorioProduto
from src.schemas.schemas import Produto
from sqlalchemy.orm import Session

router = APIRouter()

@router.post('/produtos',tags=["Produtos"], status_code=status.HTTP_201_CREATED,
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


@router.get('/produtos', tags=["Produtos"], response_model=List[Produto], )
def listar_produtos(db:Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos


@router.delete('/produtos/{id}', tags=["Produtos"], responses={
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


@router.get('/produtos/{id}', tags=["Produtos"])
def pesquisar_produto(id:int, db:Session = Depends(get_db)):
    produto = RepositorioProduto(db).pesquisar(id)
    if produto is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"produto naão encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(produto))


@router.put('/produtos/{id}', tags=["Produtos"])
def atualizar_produto(produto:Produto, id:int, db:Session = Depends(get_db)):
    produto_atualizado = RepositorioProduto(db).atualizar(id=id,produto=produto)
    if produto_atualizado is None: 
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"produto não encontrado"})
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail":"produto atualizado"})