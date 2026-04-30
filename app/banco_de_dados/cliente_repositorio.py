from app.banco_de_dados.local import BancoDeDadosLocal
from app.modelo.cliente import cliente

class ClienteRepositorio:
    def __init__(self, banco_de_dados):
        self.bd = banco_de_dados

    async def listar_clientes(self) -> list[cliente]:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email, telefone FROM clientes")
            linhas = cursor.fetchall()
            clientes = [
                cliente(id_=linha[0], 
                        nome=linha[1], 
                        email=linha[2], 
                        telefone=linha[3]
                    )
                for linha in linhas
                ]
            return clientes
    
    async def obter_cliente(self, cliente_id: int) -> cliente | None:
        with self.bd.conectar() as conexao:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, nome, email, telefone FROM clientes WHERE id = ?", (cliente_id)
                )
            linha=cursor.fetchone()
            if linha:
                return cliente(id_=linha[0], 
                        nome=linha[1], 
                        email=linha[2], 
                        telefone=linha[3]
                    )
            return None
            