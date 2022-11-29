from flask_smorest import Blueprint
from flask.views import MethodView
from libs.acoes import get_maiores, get_mais



blp = Blueprint("Acoes", "acoes", description="Retorna dados de acoes brasileiras")

@blp.route("/acoes/maiores-altas")
class maiores_altas(MethodView):
    @blp.response(200)
    def get(self):
        return get_maiores("maiores-altas")
    
    
@blp.route("/acoes/maiores-baixas")
class maiores_baixas(MethodView):
    @blp.response(200)
    def get(self):
        return get_maiores("maiores-baixas")

@blp.route("/acoes/mais-alugadas")
class mais_alugadas(MethodView):
    @blp.response(200)
    def get(self):
        return get_mais("mais-alugadas")
    
@blp.route("/acoes/mais-termadas")
class mais_termadas(MethodView):
    @blp.response(200)
    def get(self):
        return get_mais("mais-termadas")