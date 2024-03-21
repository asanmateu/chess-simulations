import os
from datetime import timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from backend.api.auth import authenticate_user, create_access_token
from backend.api.models import Game, Token
from backend.database.models import Session

app = FastAPI(
    title="Chess API",
    description="An API for playing chess",
    version="0.1",
    contact={"name": "Toni Sanmateu"},
)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session() as db:
        user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=float(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/game/")
async def create_game(game: Game):
    pass


@app.post("/game/{game_id}/move/")
async def make_move(game_id: int, move: str):
    pass


@app.get("/game/{game_id}/")
async def get_game(game_id: int):
    pass
