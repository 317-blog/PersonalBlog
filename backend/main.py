from fastapi import FastAPI
from tortoise.contrib.fastapi import RegisterTortoise

from settings import pg_config

app = FastAPI()

RegisterTortoise(app=app, config=pg_config)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', reload=True)
