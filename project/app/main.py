from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session

from app.db import init_db, get_session
from app.api.models import Song, SongCreate
from app.api import handlers

app = FastAPI()


#@app.on_event('startup')
#async def on_startup():
#    await init_db()

app.include_router(handlers.router, prefix='/songs_up')