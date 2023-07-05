# FastAPI + SQLModel + Alembic

Sample FastAPI ptoject that uses async SQLAlchemy, SQLModel, Postgres, Alembic and Docker.

# Usage

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

add a song:
```sh
$ curl -d '{"name":"Midnight Fit", "artist":"Mogwai", "year":"2021"}' -H "Content-Type: application/json" -X POST http://localhost:8004/songs
```