from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Tell FastAPI where the templates are stored
templates = Jinja2Templates(directory="core/templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"message": "Hello World from FastAPI Templates!"},
    )
