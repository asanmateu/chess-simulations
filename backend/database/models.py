from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    email = Column(String, nullable=False)
    wins = Column(Integer, default=0)
    losses = Column(Integer, default=0)


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    player1 = Column(Integer, ForeignKey('players.id'), nullable=False)
    player2 = Column(Integer, ForeignKey('players.id'), nullable=False)
    current_turn = Column(String)
    board = Column(String)

    player1 = relationship('Player', foreign_keys=[player1])
    player2 = relationship('Player', foreign_keys=[player2])


engine = create_engine('sqlite:///games.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
