from flask import Flask
from flask_restful import Api, Resource
from flask_marshmallow import Marshmallow


from resources.usuarios import RegisterUser, Users, User


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


api = Api(app)
ma = Marshmallow(app)


@app.before_first_request
def create_database():
    banco.create_all()


api.add_resource(RegisterUser, "/cadastro")
api.add_resource(Users, "/users")
api.add_resource(User, "/user/<int:id_user>")


if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)
