# models.py

from flask.ext.security import UserMixin, RoleMixin
from alfred import db

roles_users = db.Table('role_users',
        db.Column('user_id',
            db.Integer(),
            db.ForeignKey('users.id')),
        db.Column('role_id',
            db.Integer(),
            db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):

    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role',
            secondary=roles_users,
            backref=db.backref('users',
                lazy='dynamic'))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)


class Post(db.Model):

    __tablename__ = 'posts'
