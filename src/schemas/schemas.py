from typing import List, Optional
from pydantic import BaseModel #Pedido, Produto

class Usuario(BaseModel):
   id:Optional[str] = None
   nome:str
   telefone:str
   #senha:str 
#    minhas_vendas:List[Pedido]
#    meus_produtos:List[Produto]
#    meus_pedidos:List[Pedido]   

class Produto(BaseModel):
    id:Optional[str]
    nome:str
    detalhamento:str
    preco:float
    disponivel:bool = False
    #usuario:Usuario

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id:Optional[str]
    quantidade:int
    endereco_entrega:str
    entrega:bool = True
    # usuario:Usuario
    # produto:Produto
    observacoes:Optional[str] = "Sem observações"

    class Config:
        orm_mode = True



