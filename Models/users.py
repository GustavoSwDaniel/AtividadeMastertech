# pylint: disable=maybe-no-member
from sql_alchemy import banco
from datetime import datetime
from flask_marshmallow import Marshmallow

from .models import User, UserSchema, db


class UserModel(User):
    def __init__(self, nome_completo, cpf, email, data_de_cadastro):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email
        self.data_de_cadastro = datetime.strptime(data_de_cadastro, "%d/%m/%Y")

    @classmethod
    def find_user(cls, id_user):
        user = cls.query.filter_by(id_user=id_user).first()
        if user:
            return user
        return None

    @classmethod
    def find_user_name(cls, nome_completo):
        user = cls.query.filter_by(nome_completo=nome_completo).first()
        if user:
            return user
        return None

    def saver_user(self):

        db.session.add(self)
        db.session.commit()

    def updade_user(self, nome_completo, cpf, email, data_de_cadastro):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email


def serialization(user):

    userSchema = UserSchema()
    serialization_user = userSchema.dump(user)
    return serialization_user


def deserialization(user):
    userSchema = UserSchema()
    deserialization_user = userSchema.load(user)
    return deserialization_user
