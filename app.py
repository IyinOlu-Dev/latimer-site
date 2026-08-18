from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="./templates")

@app.get("/")
def read_index(request: Request):
    return templates.TemplateResponse(request, "claude.html", {})




app.mount("/static", StaticFiles(directory="./static"), name="static")