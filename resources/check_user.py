from flask_restful import Resource, reqparse, request
from datetime import datetime

from Models.models import UserSchema, user
from Models.check_user import ChckUserModel, serialization


argumentos = reqparse.RequestParser()

argumentos.add_argument(
    "usuário_responsável",
    type=str,
    required=True,
    help="Required field 'usuário_responsável'",
)

argumentos.add_argument(
    "tipo_da_batida",
    type=str,
    required=True,
    help="Required field 'tipo_da_batida'",
)

argumentos.add_argument(
    "Hora_data_batida",
    type=str,
    default=datetime.now(),
)


class RegisterCheckUser(Resource):
    def post(self, user_id):
        dados = argumentos.parse_args()
        UserCheck = ChckUserModel(user_id = user_id, **dados)

        UserCheck.saver_user()
        return {"message": user_id}
