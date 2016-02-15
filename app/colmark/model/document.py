from peewee import *
from colmark.model.base_model import BaseModel


class Document(BaseModel):
    name = CharField()

    class Meta:
        pass
