# pylint: disable=maybe-no-member
from sql_alchemy import banco

from .models import User, CheckInUserSchema, CheckIn, db


checkSchema = CheckInUserSchema()


class CheckUserModel(CheckIn):
    def __init__(self, usuario_responsavel, data_hora_batida, tipo_da_batida, user_id):

        self.usuario_responsavel = usuario_responsavel
        self.tipo_da_batida = tipo_da_batida
        self.data_hora_batida = data_hora_batida
        self.user_id = user_id

    def saver_user(self):
        db.session.add(self)
        db.session.commit()


def serialization(user):
    serialization_user = checkSchema.dump(user)
    return serialization_user


def deserialization(user):
    deserialization_user = checkSchema.load(user)
    return deserialization_user
