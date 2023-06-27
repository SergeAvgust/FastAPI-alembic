from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlmodel import Session

from app.db import init_db, get_session
from app.models import Song, SongCreate

app = FastAPI()


@app.on_event('startup')
def on_startup():
    init_db()

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}

@app.get('/songs', response_model=list[Song])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, id=song.id) for song in songs]

@app.post('/songs')
def add_song(song: SongCreate, session: Session = Depends(get_session)):
    song = Song(name=song.name, artist=song.artist)
    session.add(song)
    session.commit()
    session.refresh(song)
    return song