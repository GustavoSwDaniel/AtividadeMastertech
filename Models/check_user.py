# pylint: disable=maybe-no-member
from sql_alchemy import banco
from datetime import datetime

from .models import CheckInUserSchema, check_in, db


checkSchema = CheckInUserSchema()


class ChckUserModel(check_in):
    def __init__(self, usuário_responsável, Hora_data_batida, tipo_da_batida, user_id):
        self.usuário_responsável = usuário_responsável
        self.Hora_data_batida = Hora_data_batida
        self.tipo_da_batida = datetime.now()
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