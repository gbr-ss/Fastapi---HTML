# pip install fastapi uvicorn jinja2 python-multipart
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#roda o fastapi
#python -m uvicorn main:app --reload
app = FastAPI(title="Lista de alunos")

#Definir a pasta onde está os html
templates = Jinja2Templates(directory="templates")

#Definir a pasta onde está os arquivos estaticos (CSS, Imagens e JS)
app.mount("/static", StaticFiles(directory="static"),
name="static")

alunos = [
    {"nome": "Iago", "nota":8.5},
    {"nome": "Murilo", "nota":6.5},
    {"nome": "Joana", "nota":9.5},
    {"nome": "Francisco", "nota":0.5},
]

#Rota principal
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "lista_alunos": alunos}
    )