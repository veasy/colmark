from peewee import *
from colmark.app import database


class BaseModel(Model):
    class Meta:
        database = database