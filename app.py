from flask import Flask
from flask.views import MethodView
import marshmallow
from flask_smorest import Api, Blueprint, abort
from resources.calculadora import blp as calculadoras
from resources.acoes import blp as acoes
from resources.moedas import blp as moedas




app = Flask(__name__)
app.config["API_TITLE"] = 'Calculadora e conversor de negócios'
app.config["API_VERSION"] = 'v1'
app.config["OPENAPI_VERSION"] = '3.0.2'
app.config["DEBUG_MODE"] = True
app.config["JSON_AS_ASCII"] = False
app.config["JSONIFY_MIMETYPE"] = "application/json; charset=utf-8"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

blp = Blueprint("Calculator", "calculator", description="Operations on calculator")

@blp.route("/")
class Calculator(MethodView):
    blp.response(200)
    def get(self):
        return {"message": "Welcome to 'Renda API'!"}
    
    
api.register_blueprint(blp)
api.register_blueprint(calculadoras)
api.register_blueprint(acoes)
api.register_blueprint(moedas)
