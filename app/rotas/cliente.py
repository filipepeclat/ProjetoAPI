from fastapi import APIRouter, Depends, HTTPException
from app.modelos.cliente import Cliente
from typing import Annotated
from app.banco_de_dados.cliente_repositorio import ClienteRepositorio
from app.dependecias import obter_cliente_repositorio

CLIENTE_LIST = [Cliente(id_=1, nome="Raphael", email="raphael@rossi.com", telefone="123456789"),
                Cliente(id_=2, nome="joão", email="joao@rossi.com", telefone="987654321")]              



router = APIRouter(
    prefix="/clientes"#indica que ele sera o /clientes, então o @router.get("/") = /clientes
)

@router.get("/", response_model=list[Cliente]) #a resposta deste endpoint deve ter o formato de uma lista de objetos cliente ou seja seguindo o modelo de cliente e não um tipo padrão como string
async def listar_clientes(cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()

@router.get("/{cliente_id}", response_model=Cliente | None)
async def obter_cliente(
    cliente_repositorio: Annotated[ClienteRepositorio, Depends(obter_cliente_repositorio)], 
    cliente_id:int
):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)

    if not cliente:
            raise HTTPException(status_code=404, detail="Cliente não encontrado!")
    
    return cliente