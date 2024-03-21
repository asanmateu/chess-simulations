from typing import Optional

from pydantic import BaseModel


class Game(BaseModel):
    player1: str
    player2: str
    current_turn: Optional[str] = None
    board: Optional[str] = None
    player1_points: Optional[int] = 0
    player2_points: Optional[int] = 0
    player1_beaten_pieces: Optional[list] = []
    player2_beaten_pieces: Optional[list] = []


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    name: str
    username: str
    email: str
    disabled: Optional[bool] = None


class UserInDB(User):
    hashed_password: str
