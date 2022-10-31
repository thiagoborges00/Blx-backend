from http import HTTPStatus
from fastapi.testclient import TestClient
from src.server import app


app_test = TestClient(app)
usuario = {
    "nome":"Yroshi",
    "telefone":"8698876-1577",
    "senha":"1soai88"
}

'''testa se ao fim das 4 operacoes cadastra, lista, exclui, e cadastra novamente'''

def test_cadastrar_usuario():
    resposta = app_test.post('/usuarios', json=usuario)
    assert resposta.status_code == HTTPStatus.CREATED

def test_listagem_usuarios():
    resposta = app_test.get('/usuarios')
    assert resposta.status_code == HTTPStatus.OK

def test_remover_usuario():
    resposta = app_test.delete('/usuarios/7')
    assert resposta.status_code == HTTPStatus.OK

test_cadastrar_usuario()