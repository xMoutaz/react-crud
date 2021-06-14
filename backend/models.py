from typing import List

from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return "<User %r>" % self.name


class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UsersResponse(BaseModel):
    items: List[UserSchema]
