from http import HTTPStatus
from src.server import app
from fastapi.testclient import TestClient


app_test = TestClient(app)

produto_errado={
    "detalhament":"mesa de vidro na cor azul da marca formol",
    "disponivel":True,
    "nome":"mesa de vidro",
    "preco":20.550,
    }

produto_ok={
    "detalhamento":"mesa de vidro na cor azul da marca formol",
    "disponivel":True,
    "nome":"mesa de vidro",
    "preco":20.550,
    "usuario_id":2
    }

class TestListarProduto:

    def test_listar_produto(self):
        response =  app_test.get('/produtos')
        assert response.status_code == HTTPStatus.OK
    
    def test_listar_produto_com_url_errada(self):
        response = app_test.get('/produto')
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestCadastrarProduto:

    def test_cadastrar_produto(self):
        '''test de cadastro de produto sem id e usuario_id'''
        response =  app_test.post('/produtos',json={
            "detalhamento":"carro na cor azul da marca ford",
            "disponivel":True,
            "nome":"carro",
            "preco":22.550,
            "id":123,
        })
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


        # def test_cadastrar_produto_com_id_invalido(self):
        #     '''teste de cadastro de produto com usuario aleatorio'''
        #     response = app_test.post('/produtos', json={
        #         "detalhamento":"carro na cor azul da marca ford",
        #         "disponivel":True,
        #         "nome":"carro",
        #         "preco":22.550,
        #         "id":123,
        #         "usuario_id":122
        #     })

        #     assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        #     #verificar se o usuario_id do payload existe antes de cadastrar

    def test_cadastrar_produto_obj_errado(self):
        '''teste de cadastro de produto com payload errado'''
        response = app_test.post('/produtos',json=produto_errado)
        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


    def test_cadastrar_produto_feliz(self):
        '''teste de cadastro de produto do caminho feliz'''
        response = app_test.post('/produtos', json=produto_ok, )
        assert response.status_code == HTTPStatus.OK


    def test_cadastrar_produto_url_errada(self):
        '''teste de cadastro de produto passando url errada'''
        response = app_test.post('/produto', json=produto_ok)
        assert response.status_code == HTTPStatus.NOT_FOUND


class TestRemoverProduto:

    def test_remover_produto(self):
        '''teste de remocao de produto com tudo certo'''
        response = app_test.delete('/produtos/5')
        assert response.status_code == HTTPStatus.OK


    def test_remover_produto_url_errada(self):
        '''teste de remocao de produto passando url errada'''
        resposta = app_test.delete('/produto/4')
        assert resposta.status_code == HTTPStatus.NOT_FOUND


    def test_remover_produto_com_id_n_cadastrado(self):
        '''teste de remocao de produto com id nao cadastrado'''
        resposta = app_test.delete('/produtos/400')
        assert resposta.status_code == HTTPStatus.NOT_FOUND

    
    def test_remover_produto_com_id_invalido(self):
        '''teste de remocao de produto com id nao cadastrado'''
        resposta = app_test.delete('/produtos/jas453')
        assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


class TestPesquisarProduto:

    def test_pesquisa_certa(self):
        '''teste de pesquisa de produto no caminho feliz'''
        resposta = app_test.get('/produtos/3')
        assert resposta.status_code == HTTPStatus.OK
        assert resposta.json() == {
    "id": 3,
    "preco": 3.5,
    "disponivel": True,
    "nome": "mamão com acucar",
    "detalhamento": "mistura de mamão papaya com acucar granulado",
    "usuario_id": 3
}


    def test_pesquisa_url_errada(self):
        '''teste de pesquisa de produto com url errada'''
        resposta = app_test.get('/produto/213')
        assert resposta.status_code == HTTPStatus.NOT_FOUND
        assert resposta.json() == {"detail":"Not Found"}


    def test_pesquisa_id_n_cadastrado(self):
        '''teste de pesquisa de produto com id nao cadastrado'''
        resposta = app_test.get('/produtos/213')
        assert resposta.status_code == HTTPStatus.NOT_FOUND


    def test_pesquisa_id_invalido(self):
        '''teste de pesquisa de produto com id invalido'''
        resposta = app_test.get('/produtos/lahsu661669')
        assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


class TestUpdateProduto:

    payload = {
        "nome":"camaraoo internacional",
        "detalhamento":"camarao tropical com molho branco e salsicha",
        "preco":155.50,
        "disponivel":True
    }

    payload_errado = {
        "nome":"fondue",
        "detalhamento":"nunca nem vi",
        "preco":59.40,
        "disponviel":True
    }

    def test_atualizar_produto(self):
        '''teste de atualizar produto pelo caminho feliz'''
        resposta = app_test.put('/produtos/3', json=self.payload)
        assert resposta.status_code == HTTPStatus.OK
        assert resposta.json() == {"detail": "produto atualizado"}


    def test_atualizar_produto_url_errada(self):
        ''' teste de atualizacao de produto com put e url errada'''
        resposta = app_test.put('/produti/3', json=self.payload)
        assert resposta.status_code == HTTPStatus.NOT_FOUND
        assert resposta.json() == {"detail":"Not Found"}


    def test_atualizar_produto_id_invalido(self):
        '''teste de atualizacao de produto com id nao numerico'''
        resposta = app_test.put('/produtos/54ç', json=self.payload)
        assert resposta.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


    def test_atualizar_produto_id_n_cadastrado(self):
        '''teste de atualizacao de produto nao cadastrado'''
        resposta = app_test.put('/produtos/687', json=produto_ok)
        assert resposta.status_code == HTTPStatus.NOT_FOUND
        assert resposta.json() == {"detail":"produto não encontrado"}
         