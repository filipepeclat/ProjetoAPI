from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.rotas import cliente

app = FastAPI(
    title="techlog Solutions API", #nome da aplicação
    description="CRM para techlog Solutions",
    version="1.0.0",
)#acessivel pelo /docs

@app.get("/") # indica o que vai aparecer quando acessar o http://127.0.0.1:8000/ (pagina inicial)
async def helth_check(): # por convenção os end points são assincronos
    return {"status": "Ok"}

@app.get("/front", response_class=HTMLResponse) #ao inves de retornar um json vai retornar um html
async def front_page():
    html_content= """ 
<h1>Olá</h1>
<p>Minha página</p>
"""
    return html_content

app.include_router(cliente.router)