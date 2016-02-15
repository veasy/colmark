from peewee import *
from colmark.model.base_model import BaseModel


class User(BaseModel):
    username = CharField()
    birthday = DateField()

    class Meta:
        pass
