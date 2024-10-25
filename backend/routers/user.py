from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from backend.models.user import User as db_User
from backend.routers import templates


user_router = APIRouter()


@user_router.get('/')
async def get_users(request: Request):
    users = await db_User.all()
    if users:
        return templates.TemplateResponse(
            'index.html',
            {'request': request,
             'users': users}
        )


