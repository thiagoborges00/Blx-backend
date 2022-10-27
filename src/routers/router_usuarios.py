from typing import List
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from fastapi import APIRouter, status, Depends, Path
from src.infra.sqlAlchemy.config.database import get_db
from src.infra.sqlAlchemy.repositorys.usuario import RepositorioUsuario
from src.schemas.schemas import Usuario, UsuarioSimples

router = APIRouter()

@router.get('/usuarios', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=List[Usuario])
def listar_usuarios(db:Session = Depends(get_db)):
    usuarios = RepositorioUsuario(db).listar()
    return usuarios


@router.post('/usuarios', tags=["Usuarios"], status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar_usuario(user:Usuario, db:Session = Depends(get_db)):
    novo_usuario = RepositorioUsuario(db).criar(user)
    return novo_usuario


@router.delete('/usuarios/{id}', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=UsuarioSimples)
def remover_usuario(id:int = Path(..., ge=1), db:Session = Depends(get_db)):
    deletado = RepositorioUsuario(db).remover(id)
    if deletado is None: return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"usuário não encontrado"})
    return deletado


@router.get('/usuarios/{id}', tags=["Usuarios"], status_code=status.HTTP_200_OK, response_model=Usuario)
def pesquisar_usuario(id:int = Path(..., title="identificador único",ge=1) , db:Session = Depends(get_db)):
    usuario = RepositorioUsuario(db).pesquisar(id)
    if not usuario : return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"detail":"usuário não encontrado"})
    return usuario