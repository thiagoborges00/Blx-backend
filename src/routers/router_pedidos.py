from typing import List
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.infra.sqlAlchemy.config.database import get_db
from src.infra.sqlAlchemy.repositorys.pedido import RepositorioPedido
from src.schemas.schemas import Pedido
from sqlalchemy.orm import Session


router = APIRouter()

#PEDIDOS
@router.get('/pedidos', tags=["Pedidos"])
def listar_pedidos(db:Session = Depends(get_db)):
    pedidos = RepositorioPedido(db).listar()
    return pedidos


@router.post('/pedidos', tags=["Pedidos"])
def cadastrar_pedido(pedido:Pedido, db:Session = Depends(get_db)):
    pedido = RepositorioPedido(db).cadastrar(pedido)
    return pedido