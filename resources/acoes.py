from flask_smorest import Blueprint
from flask.views import MethodView
from libs.acoes import get_maiores, get_mais



blp = Blueprint("Acoes", "acoes", description="Retorna dados de acoes brasileiras")

@blp.route("/acoes/maiores-altas")

class maiores_altas(MethodView):
    """Retorna as ações que mais valorizaram no dia 
    (pesquisa atualizada as 7h da manhã)"""
    @blp.response(200)
    def get(self):
        return get_maiores("maiores-altas")
    
    
@blp.route("/acoes/maiores-baixas")
class maiores_baixas(MethodView):
    """Retorna as ações que mais desvalorizaram no dia 
    (pesquisa atualizada as 7h da manhã)"""
    @blp.response(200)
    def get(self):
        return get_maiores("maiores-baixas")

@blp.route("/acoes/mais-alugadas")
class mais_alugadas(MethodView):
    """Retorna as ações mais populares 
    (pesquisa atualizada as 7h da manhã)"""
    @blp.response(200)
    def get(self):
        return get_mais("mais-alugadas")
    
@blp.route("/acoes/mais-termadas")
class mais_termadas(MethodView):
    """Retorna as ações mais termadas 
    (pesquisa atualizada as 7h da manhã)"""
    @blp.response(200)
    def get(self):
        return get_mais("mais-termadas")