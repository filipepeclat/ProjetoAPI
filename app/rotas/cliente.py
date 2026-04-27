from fastapi import APIRouter
from app.modelo.cliente import cliente

CLIENTE_LIST = [cliente(id_=1, nome="Raphael", email="raphael@rossi.com", telefone="123456789"),
                     cliente(id_=2, nome="joão", email="joao@rossi.com", telefone="987654321")]              



router = APIRouter(
    prefix="/clientes"#indica que ele sera o /clientes, então o @router.get("/") = /clientes
)

@router.get("/", response_model=list[cliente]) #a resposta deste endpoint deve ter o formato de uma lista de objetos cliente ou seja seguindo o modelo de cliente e não um tipo padrão como string
async def listar_clientes():

    return CLIENTE_LIST

@router.get("/{cliente_id}", response_model=cliente | None)
async def obter_cliente(cliente_id:int):
    for cliente in CLIENTE_LIST:
        if cliente.id_ == cliente_id:
            return cliente 
    return None