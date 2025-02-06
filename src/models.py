import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla de usuarios
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)

# Tabla de planetas
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    favorites = relationship("Favorite") 

# Tabla de personajes
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    gender = Column(String(50))
    species = Column(String(250))
    birth_year = Column(String(50))
    favorites = relationship("Favorite")  

# Tabla de favoritos
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    created_at = Column(DateTime)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
