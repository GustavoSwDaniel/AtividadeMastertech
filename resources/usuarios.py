from flask_restful import Resource,reqparse, request
from datetime import datetime


from Models.usuarios import UserModel, UserSchema, serialization, deserialization


userSchema = UserSchema()


argumentos = reqparse.RequestParser()
    
argumentos.add_argument('nome_completo', 
                                type=str, 
                                required = True, 
                                help="Required field 'nome'")
argumentos.add_argument('cpf', 
                                type=str,
                                required = True,
                                help="Required field 'cpf'")

argumentos.add_argument('email',
                                type=str, 
                                required=True, 
                                help="Required field 'email'")
    
argumentos.add_argument('data_de_cadastro',                           
                                type=str,
                                help="Required field 'date'")



class Users(Resource):
    def get(self):
        return [userSchema.dump(user) for user in UserModel.query.all()]


class RegisterUser(Resource):

    
    def post (self):
        
        dados = argumentos.parse_args()
        user = UserModel(**dados)
       
        user.saver_user()
        return serialization(user)


class User(Resource):
    
    argumentos = reqparse.RequestParser()
    
    argumentos.add_argument('nome_completo', 
                                type=str, 
                                required = True, 
                                help="Required field 'nome'")
    argumentos.add_argument('cpf', 
                                type=str,
                                required = True,
                                help="Required field 'cpf'")

    argumentos.add_argument('email',
                                type=str, 
                                required=True, 
                                help="Required field 'email'")

    argumentos.add_argument('data_de_cadastro',                           
                                type=str,
                                help="Required field 'date'")
    
    def get(self,id_user):
        user = UserModel.find_user(id_user)
        if user:
            return serialization(user), 200
        return {'message':'User not found'}, 404


    def put(self, id_user):

        dados = User.argumentos.parse_args()

        user_encontrado = UserModel.find_user(id_user)
        print("0" *50)
        print(user_encontrado)
        print(dados)
        print("0" *50)

        
        if user_encontrado:
            user_encontrado.updade_user(**dados)
            try:
                user_encontrado.saver_user()
            except:
                return {'message': 'interenal error'}, 500
            return serialization(user_encontrado)
        return {'message': 'user not found'}, 404
        
