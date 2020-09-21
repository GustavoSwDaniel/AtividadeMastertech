from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from datetime import datetime

# pylint: disable=maybe-no-member

ma = Marshmallow()
db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):

    __tablename__ = "users"

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    data_de_cadastro = db.Column(db.Date)
    checkInUser = db.relationship("CheckIn", backref="users", lazy=True)


class CheckIn(db.Model):

    __tablename__ = "checks"

    id_pont = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_responsavel = db.Column(db.String(30))
    tipo_da_batida = db.Column(db.String(30))
    data_hora_batida = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id_user"))


class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id_user", "nome_completo", "cpf", "email", "data_de_cadastro")


class CheckInUserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id_pont",
            "usuario_responsavel",
            "tipo_da_batida",
            "data_hora_batida",
            "id_user",
        )
