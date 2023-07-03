from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select

from app.api.models import Song, SongCreate

async def get_all(session: Session):
    result = await session.execute(select(Song))
    songs = result.scalars().all()
    return [Song(name=song.name, artist=song.artist, year=song.year, id=song.id) for song in songs]

async def post(payload: SongCreate, session: Session):
    song = Song(name=payload.name, artist=payload.artist, year=payload.year)
    session.add(song)
    await session.commit()
    await session.refresh(song)
    return song