from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routers import utilsws

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(utilsws.router)
templates = Jinja2Templates(directory="templates")
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )