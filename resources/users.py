from flask_restful import Resource, reqparse, request
from datetime import datetime

from Models.models import UserSchema, User
from Models.users import UserModel, serialization

userSchema = UserSchema()


argumentos = reqparse.RequestParser()

argumentos.add_argument(
    "nome_completo", type=str, required=True, help="Required field 'nome'"
)
argumentos.add_argument("cpf", type=str, required=True, help="Required field 'cpf'")

argumentos.add_argument("email", type=str, required=True, help="Required field 'email'")

argumentos.add_argument(
    "data_de_cadastro", default=datetime.now(), type=str, help="Required field 'date'"
)


class Users(Resource):
    def get(self):
        return [serialization(User) for User in User.query.all()]


class Hello(Resource):
    def get(self, teste):
        return {"message": teste}


class RegisterUser(Resource):
    def post(self):

        dados = argumentos.parse_args()
        userR = UserModel(**dados)
        try:
            userR.saver_user()
            return serialization(userR), 201
        except:
            return {"message": "Internal error"}, 500


class UserFind(Resource):
    def get(self, id_user):
        userG = UserModel.find_user(id_user)
        if userG:
            return serialization(userG), 200
        return {"message": "User not found"}, 404

    def put(self, id_user):

        dados = argumentos.parse_args()

        user_foun = UserModel.find_user(id_user)

        if user_foun:
            user_foun.updade_user(**dados)
            try:
                user_foun.saver_user()
            except:
                return {"message": "interenal error"}, 500
            return serialization(user_foun)
        return {"message": "user not found"}, 404