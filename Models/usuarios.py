from sql_alchemy import banco
from datetime import datetime
from flask_marshmallow import Marshmallow

ma = Marshmallow()

# pylint: disable=maybe-no-member


class UserModel(banco.Model):

    __tablename__ = "users"

    id_user = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome_completo = banco.Column(banco.String(100))
    cpf = banco.Column(banco.String(11))
    email = banco.Column(banco.String(50))
    data_de_cadastro = banco.Column(banco.Date)

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

    def saver_user(self):

        banco.session.add(self)
        banco.session.commit()

    def updade_user(self, nome_completo, cpf, email, data_de_cadastro):
        self.nome_completo = nome_completo
        self.cpf = cpf
        self.email = email


class UserSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("id_user", "nome_completo", "cpf", "email", "data_de_cadastro")


def serialization(user):
    userSchema = UserSchema()
    serialization_user = userSchema.dump(user)
    return serialization_user


def deserialization(user):
    userSchema = UserSchema()
    deserialization_user = userSchema.load(user)
    return deserialization_user
