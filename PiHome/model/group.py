# -*- code: utf-8 -*-
# user.py
from PiHome import db
from model import BaseDB


class Group(BaseDB):
    """
        Modelo de datos de los grupos
    """

    #: Nombre de tabla
    __tablename__ = 'groups'

    category = db.Column(
        db.String(25),
        nullable=False,
        unique=True)
    definition = db.Column(db.Text())

    def __init__(self, category=None, definition=None, **kwargs):
        super(Group, self).__init__(**kwargs)
        self.category = category
        self.definition = definition
