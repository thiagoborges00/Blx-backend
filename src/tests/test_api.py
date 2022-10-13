from http import HTTPStatus
import os
import sys
#from fastapi import Depends
#from src.infra.sqlAlchemy.config.database import get_db
#from src.schemas.schemas import Pedido, Produto
from src.server import app
from fastapi.testclient import TestClient
#from sqlalchemy.orm import Session
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app_test = TestClient(app)
# produto1 = Produto(detalhamento='carro na cor azul da marca ford',
#                 disponivel=True,
#                 nome='carro',
#                 preco=22.550,
#                 id=123)

# pedido = Pedido(endereco_entrega='rua damasceno lopo 123',
#                 entrega=True,
#                 id=12,
#                 observacoes="ultima casa do quitinet",
#                 quantidade=2)

# def test_cadastrar_produto(produto1:Produto, db:Session = Depends(get_db)):
#     response =  app_test.post('/produtos')
#     assert response.status_code == HTTPStatus.CREATED

def test_listar_produto():
    response =  app_test.get('/produtos')
    assert response.status_code == HTTPStatus.OK


def test_cadastrar_produto():
    response =  app_test.post('/produtos',json={
        "detalhamento":"carro na cor azul da marca ford",
        "disponivel":True,
        "nome":"carro",
        "preco":22.550,
        "id":123
    })
    assert response.status_code == HTTPStatus.OK
