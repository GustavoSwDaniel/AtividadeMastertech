# pylint: disable=maybe-no-member
from sql_alchemy import banco
from sqlalchemy.orm import join
from datetime import datetime

from .models import User, CheckInUserSchema, CheckIn, db


checkSchema = CheckInUserSchema()


class CheckUserModel(CheckIn):
    def __init__(self, usuario_responsavel, hora_data_batida, tipo_da_batida, user_id):
        self.usuario_responsavel = usuario_responsavel
        self.hora_data_batida = hora_data_batida
        self.tipo_da_batida = tipo_da_batida
        self.user_id = user_id

    @classmethod
    def find_checks(cls):
        user = User()
        checkin = CheckIn()
        checks = (
            db.query(checkin).join(user).filter(user.id_user == checkin.user_id).all()
        )

        if checks:
            return checks
        return None

    def saver_user(self):
        db.session.add(self)
        db.session.commit()


def serialization(user):
    serialization_user = checkSchema.dump(user)
    return serialization_user


def deserialization(user):
    deserialization_user = checkSchema.load(user)
    return deserialization_user