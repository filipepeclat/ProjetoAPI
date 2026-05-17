from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from app.rotas import cliente
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="techlog Solutions API", #nome da aplicação
    description="CRM para techlog Solutions",
    version="1.0.0",
)#acessivel pelo /docs

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(cliente.router)

@app.get("/health") # indica o que vai aparecer quando acessar o http://127.0.0.1:8000/ (pagina inicial)
async def health_check(): # por convenção os end points são assincronos
    return {"status": "Ok"}

@app.get("/")
async def front_page(request: Request):
    session_token = request.cookies.get("session_token")

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "session_token": session_token,
            "versao": app.version}
    )

'''@app.get("/")
async def front_page(request: Request):
    session_token = request.cookies.get("session_token")

    return templates.TemplateResponse("index.html", {
        "request": request,
        "titulo": "Techlog Solutions CRM",
        "versao": "1.0.0",
        "session_token": session_token
    })'''