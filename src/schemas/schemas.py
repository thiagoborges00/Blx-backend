from typing import List, Optional
from pydantic import BaseModel, validator


class ProdutoSimples(BaseModel):
    id:int
    nome:str
    detalhamento:str
    preco:float

    class Config:
        orm_mode = True


class Usuario(BaseModel):
    id:Optional[int] = None
    nome:str
    telefone:str
    senha:str 
    produtos:List[ProdutoSimples] = []
#    minhas_vendas:List[Pedido]
#    meus_produtos:List[Produto]
#    meus_pedidos:List[Pedido]  
    class Config:
        orm_mode = True


class UsuarioResponse(BaseModel):
    id:str
    nome:str
   
    class Config:
        orm_mode = True


class UsuarioSimples(BaseModel):
    msg:str = "usuario deletado com sucesso"
    id:str
    nome:str
   
    class Config:
        orm_mode = True


class Produto(BaseModel):
    id:Optional[int]
    nome:str
    detalhamento:str
    preco:float
    disponivel:bool = False
    usuario_id:Optional[int]
    usuarios:Optional[UsuarioResponse] # campo utilizado para mostrar detalhes do relacionamento na listagem


    # @validator('preco')
    # def id_valid(cls, v):
    #     pdb.set_trace()
    #     if not isinstance(v, float):
    #         raise ValueError('parametro real não informado')

    # @validator('usuario_id')
    # def user_id_valid(cls, v):
    #     if not isinstance(v, int):
    #         raise ValueError('não é um inteiro')
    #     return v



    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "nome": "Pizza",
                "detalhamento": "pizza de carne de sol com banana no tamanho GG",
                "preco": 65.4,
                "disponivel": True,
                "usuario_id": 4 
            }
        }


class Pedido(BaseModel):
    id:Optional[int]
    quantidade:int
    endereco_entrega:str
    entrega:bool = True
    # usuario:Usuario
    # produto:Produto
    observacoes:Optional[str] = "Sem observações"

    class Config:
        orm_mode = True