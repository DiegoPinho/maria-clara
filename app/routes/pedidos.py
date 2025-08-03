
from fastapi import APIRouter, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
from app.schemas.pedido import PedidoCreate, Item
from app.datasources.mongo import db
from bson.objectid import ObjectId

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/pedidos", response_class=HTMLResponse)
async def listar_pedidos(
    request: Request,
    nome: str = Query(None),
    data_inicio: str = Query(None),
    data_fim: str = Query(None),
    page: int = Query(1)
):
    query = {}
    if nome:
        query["nome_cliente"] = {"$regex": nome, "$options": "i"}
    if data_inicio and data_fim:
        query["data_pedido"] = {
            "$gte": datetime.fromisoformat(data_inicio),
            "$lte": datetime.fromisoformat(data_fim)
        }
    page_size = 10
    skip = (page - 1) * page_size
    pedidos = await db.pedidos.find(query).skip(skip).limit(page_size).to_list(page_size)
    total = await db.pedidos.count_documents(query)
    return templates.TemplateResponse("pedidos.html", {
        "request": request,
        "pedidos": pedidos,
        "nome": nome or "",
        "data_inicio": data_inicio or "",
        "data_fim": data_fim or "",
        "page": page,
        "total_pages": (total // page_size) + int(total % page_size > 0)
    })

@router.get("/pedidos/novo", response_class=HTMLResponse)
async def novo_pedido(request: Request):
    return templates.TemplateResponse("novo_pedido.html", {"request": request})

@router.post("/pedidos")
async def criar_pedido(
    nome_cliente: str = Form(...),
    email_cliente: str = Form(...),
    data_pedido: str = Form(...),
    item_nome: list[str] = Form(...),
    item_quantidade: list[int] = Form(...),
    item_preco_unitario: list[float] = Form(...)
):
    itens = []
    for nome, qtd, preco in zip(item_nome, item_quantidade, item_preco_unitario):
        itens.append({
            "nome": nome,
            "quantidade": qtd,
            "preco_unitario": preco
        })
    pedido = {
        "nome_cliente": nome_cliente,
        "email_cliente": email_cliente,
        "data_pedido": datetime.fromisoformat(data_pedido),
        "itens": itens
    }
    await db.pedidos.insert_one(pedido)
    return RedirectResponse(url="/pedidos", status_code=303)

@router.get("/pedidos/{pedido_id}", response_class=HTMLResponse)
async def detalhe_pedido(request: Request, pedido_id: str):
    pedido = await db.pedidos.find_one({"_id": ObjectId(pedido_id)})
    return templates.TemplateResponse("detalhe_pedido.html", {"request": request, "pedido": pedido})

@router.post("/pedidos/{pedido_id}/delete")
async def excluir_pedido(pedido_id: str):
    await db.pedidos.delete_one({"_id": ObjectId(pedido_id)})
    return RedirectResponse(url="/pedidos", status_code=303)
