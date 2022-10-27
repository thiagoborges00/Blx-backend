from fastapi import FastAPI
from src.routers import router_pedidos,router_produtos, router_usuarios

app = FastAPI()

app.include_router(router_produtos.router)
app.include_router(router_pedidos.router)
app.include_router(router_usuarios.router)