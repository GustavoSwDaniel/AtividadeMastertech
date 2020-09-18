from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# pylint: disable=maybe-no-member

ma = Marshmallow()
db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class user(db.Model):

    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_completo = db.Column(db.String(100))
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(50))
    data_de_cadastro = db.Column(db.Date)
    checkInUser = db.relationship("check_in", backref="user")


class check_in(db.Model):

    id_pont = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuário_responsável = db.Column(db.String(30))
    tipo_da_batida = db.Column(db.String(30))
    Hora_data_batida = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id_user"))


class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id_user", "nome_completo", "cpf", "email", "data_de_cadastro")


class CheckInUserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = (
            "id_pont",
            "usuário_responsável",
            "tipo_da_batida",
            "Hora_data_batida",
            "id_user",
        )
