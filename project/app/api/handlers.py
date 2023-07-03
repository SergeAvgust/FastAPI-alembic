from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db import get_session
from app.api import crud
from app.api.models import Song, SongBase, SongCreate

router = APIRouter()

@router.get('', response_model=list[Song])
async def get_songs(session: Session = Depends(get_session)):
    return await crud.get_all(session=session)

@router.post('', response_model=Song)
async def add_song(payload: SongCreate, session: Session = Depends(get_session)):
    song_inserted = await crud.post(payload, session=session)
    return song_inserted