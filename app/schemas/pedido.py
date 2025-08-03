
from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class Item(BaseModel):
    nome: str
    quantidade: int
    preco_unitario: float

class PedidoCreate(BaseModel):
    nome_cliente: str
    email_cliente: EmailStr
    data_pedido: datetime
    itens: List[Item]
