from flask_smorest import Blueprint
from flask.views import MethodView
from libs.moedas import get_valor_moeda, get_valor_criptomoeda

blp = Blueprint("Moedas", "moedas", description=
                "Retorna os valores das principais moedas do mundo")

@blp.route("/moedas/dolar-americano")
class Dolar_americano(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("dolar-americano")

@blp.route("/moedas/euro")
class Euro(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("euro")

@blp.route("/moedas/libra-esterlina")
class Libra_esterlina(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("libra-esterlina")

@blp.route("/moedas/iene")
class Iene(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("iene")

@blp.route("/moedas/dolar-australiano")
class Dolar_australiano(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("dolar-australiano")

@blp.route("/moedas/franco-suico")
class Franco_suico(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("franco-suico")

@blp.route("/moedas/dolar-canadense")
class Dolar_canadense(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("dolar-canadense")

@blp.route("/moedas/yuan")
class Yuan(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("yuan")

@blp.route("/moedas/peso-argentino")
class Peso_argentino(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("peso-argentino")

@blp.route("/moedas/lira-turca")
class Lira_turca(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_moeda("lira-turca")

@blp.route("/moedas/bitcoin")
class Bitcoin(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_criptomoeda("bitcoin")

@blp.route("/moedas/ethereum")
class Ethereum(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_criptomoeda("ethereum")

@blp.route("/moedas/tether")
class Tether(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_criptomoeda("tether")

@blp.route("/moedas/dogecoin")
class Dogecoin(MethodView):
    @blp.response(200)
    def get(self):
        return get_valor_criptomoeda("dogecoin")


