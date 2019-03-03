# -*- code: utf-8 -*-
# controller.goup

# Define the blueprint: 'user', set its url prefix: app.url/auth
from flask import Blueprint, render_template, session

from model import User, Group

group_ctr = Blueprint('group', __name__, url_prefix='/group')


@group_ctr.route('/show', methods=['GET'])
@group_ctr.route('/show/<int:page>', methods=['GET'])
def show(page=1):
    """
        Muestra la información de 'users'
    """
    per_page = 5
    users = User.query.join('group').add_columns(
        User.name,
        User.email,
        Group.category)  # .paginate(page,per_page,False)
    return render_template('show.html',
                           title='Mostrando prueba de lista',
                           results=users,
                           table='users',
                           category=session['category'])
