from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from app.rotas import cliente, login, registro
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.autenticacao_middleware import AuthenticationToken



templates = Jinja2Templates(directory="templates")

app = FastAPI(
    title="techlog Solutions API", #nome da aplicação
    description="CRM para techlog Solutions",
    version="1.0.0",
)#acessivel pelo /docs

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(cliente.router)
app.include_router(cliente.front_router)
app.include_router(login.router)
app.include_router(registro.router)
app.add_middleware(AuthenticationToken)

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
            "versao": app.version
        }
    )
@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("session_token")
    return response
