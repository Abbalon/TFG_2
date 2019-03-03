# -*- code: utf-8 -*-
# model
"""
Clase que declara e instancia la conexxión con la base de datos
"""

from PiHome import db


class BaseDB(db.Model):
    """
    Define los elementos comunes a todas las tablas que lo heredarán
    """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


from model.user import User
from model.group import Group


def __create_foreign_keys():
    """
        Establece el estado básico de la BD
    """

    group = Group.query.filter_by(id='1').first()
    if group is None:
        std_group = Group(
            category='Estandar',
            definition='Usuario estándar, puede hacer uso del sistema de control de acceso.'
        )

        wd_group = Group(
            category='WatchDog',
            definition='Usuario vigilante, usuario estándar con permisos remotos y visualización de logs.'
        )

        adm_group = Group(
            category='Admin',
            definition='Admin'
        )

        # Usuario principal para poder deplegar la aplicación
        admin = User(
            name='admin',
            password='admin',
            email='PiDomoticTFG+admin@gmail.com',
            group=adm_group,
            validated=True)

        db.session.add(std_group)
        db.session.add(wd_group)
        db.session.add(adm_group)
        db.session.add(admin)

        print("Commit")
        db.session.commit()
