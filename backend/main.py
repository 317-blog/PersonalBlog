from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from tortoise.contrib.fastapi import RegisterTortoise

from settings import pg_config
from routers.user import user_router
from routers import templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="test/static"))
RegisterTortoise(app=app, config=pg_config)

app.include_router(user_router, prefix="/user", tags=["User"])


@app.get("/index")
async def index(request: Request):
    name = "root"
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "user": name,
        }
    )


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
