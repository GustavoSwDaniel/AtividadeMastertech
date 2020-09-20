# pylint: disable=maybe-no-member
from flask import Flask
from flask_restful import Api, Resource
from flask_migrate import Migrate


from Models.models import configure as config_db
from resources.users import RegisterUser, Users, UserFind, Hello
from resources.check_user import RegisterCheckUser, ListUser


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True


api = Api(app)

config_db(app)

Migrate(app, app.db)


api.add_resource(Hello, "/hello/<int:teste>")
api.add_resource(RegisterUser, "/cadastro")
api.add_resource(Users, "/users")
api.add_resource(UserFind, "/user/<int:id_user>")

api.add_resource(RegisterCheckUser, "/point/<int:user_id>")
api.add_resource(ListUser, "/checks/<int:id_user>")


if __name__ == "__main__":
    from sql_alchemy import banco

    banco.init_app(app)
    app.run(debug=True)