from pydantic import BaseModel

class cliente(BaseModel): #BseModel gera um json ou um dicionario e faz conversão de tipos como string -> int
    id_: int #por o id ser um buit-in é necessario colocar o _
    nome: str
    email: str
    telefone: str