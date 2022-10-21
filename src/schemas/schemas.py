from typing import List, Optional
from pydantic import BaseModel


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

    class Config:
        orm_mode = True


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