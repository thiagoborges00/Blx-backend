from sqlalchemy.orm import Session
from src.schemas.schemas import Usuario
from src.infra.sqlAlchemy.models import models

class RepositorioUsuario():
    
    def __init__(self, db:Session):
        self.db = db

    def criar(self, user:Usuario):

        usuario = models.Usuario(nome=user.nome,
                          senha=user.senha,
                          telefone=user.telefone,
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    def listar(self):
        usuarios_ativos = self.db.query(models.Usuario).all()
        return usuarios_ativos
    
    def pesquisar(self, id:int):
        usuario = self.db.get(models.Usuario, id)
        return usuario
    
    def remover(self, id:int):
        usuario = self.pesquisar(id)
        if usuario:
            self.db.delete(usuario)
            self.db.commit()
        return usuario