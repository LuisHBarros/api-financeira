
from libs import calculos
from flask_smorest import Blueprint
from flask.views import MethodView

from schema import IrSchema, InssSchema

blp = Blueprint("Calculadoras", "calculadoras", description="Calculadoras para Imposto de Renda e INSS")





@blp.route("/imposto_renda")
class imposto_renda(MethodView):
    @blp.arguments(IrSchema)
    @blp.response(200)
    def get(self, renda_data):
        """Recebe o salario, os dependentes, as despesas
        em educação, saúde, pensão, previdência e doações,
        e devolve o imposto de renda (Usando dados validos de 2022)
        """
        dependentes = round(calculos.dependentes(float(renda_data["dependentes"])), 2)
        salario = float(renda_data["salario"])
        educacao = calculos.educacao(float(renda_data["educacao"]), int(renda_data["dependentes"]))
        pensao = float(renda_data["pensao"])
        saude = float(renda_data["saude"])
        previdencia = float(renda_data["previdencia"]) * 0.12
        livro_caixa = float(renda_data["livro_caixa"])
        doacoes = float(renda_data["doacoes"])
        salario = float(renda_data["salario"])
        inss = round(calculos.inss(salario), 2)
        deducao = educacao + pensao + previdencia + livro_caixa + doacoes + saude
        ir = round(calculos.imposto_renda(salario, dependentes, inss, deducao), 2)
        return {"imposto_de_renda " : f"R${ir}"}
        
@blp.route("/inss")
class INSS(MethodView):
    """Recebe o salario mensal e devolve o imposto do INSS (Usando dados validos de 2022) """
    @blp.arguments(InssSchema)
    @blp.response(200)
    def get(self, renda_data):
        salario = renda_data['salario']
        inss = round(calculos.inss(salario),2)
        return {"INSS": f"R${inss}"}