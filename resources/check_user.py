from flask_restful import Resource, reqparse, request
from datetime import datetime
from collections import OrderedDict

from Models.models import UserSchema, User, CheckIn
from Models.check_user import CheckUserModel, serialization
from Models.users import UserModel

tipo_de_batidas = ("Entrada", "Saida")

argumentos = reqparse.RequestParser()

argumentos.add_argument(
    "usuario_responsavel",
    type=str,
    required=True,
    help="Required field 'usuario_responsavel'",
)

argumentos.add_argument(
    "tipo_da_batida",
    type=str,
    required=True,
    choices=tipo_de_batidas,
    help="Option invalid! Saida/Entrada",
)

argumentos.add_argument(
    "hora_data_batida",
    type=str,
    default=datetime.now(),
)


class RegisterCheckUser(Resource):
    def post(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            dados = argumentos.parse_args()
            UserCheck = CheckUserModel(user_id=user_id, **dados)

            UserCheck.saver_user()
            return serialization(UserCheck), 200
        return {"message": "User not found"}, 404


class ListUser(Resource):

    argumentos = reqparse.RequestParser()

    argumentos.add_argument(
        "nome_completo",
        type=str,
        required=True,
        help="Required field 'nome_completo'",
    )

    def get(self):
        """return [serialization(check_in) for check_in in user.query.all()]"""
        check = CheckUserModel.find_checks()
        return serialization(check)