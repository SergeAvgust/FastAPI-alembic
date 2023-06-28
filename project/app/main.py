from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session

from app.db import init_db, get_session
from app.models import Song, SongCreate

app = FastAPI()


@app.on_event('startup')
async def on_startup():
    await init_db()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get('/songs', response_model=list[Song])
async def get_songs(session: Session = Depends(get_session)):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]

@app.post('/songs')
async def add_song(song: SongCreate, session: Session = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song