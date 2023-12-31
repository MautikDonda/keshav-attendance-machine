from datetime import datetime

import uuid

import starlette.responses
from fastapi import FastAPI
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from app import api
from app.db import database
from app.db.models import create_tables
from app.util.logger import logger

app = FastAPI(
    title="Keshav Attendance Machine APIs",
    version="1.0",
)

app.include_router(api.router)


@app.on_event("startup")
async def startup():
    create_tables()


@app.middleware("http")
async def add_cors_header(request, call_next):
    uid = uuid.uuid4()
    logger.info(f"Request: {uid}\t{request.method}\t{request.url}\t{request.headers}\t{request.query_params}")
    database.connect(True)
    start_time = datetime.now()
    response: starlette.responses.Response = await call_next(request)
    logger.info(f"Response: {uid}\t{response.status_code}")
    response.headers['X-Process-Time'] = str((datetime.now() - start_time).microseconds / 1000)
    database.close()
    return response


@app.get('/index')
def index():
    with open('config.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(html_content, 200)
