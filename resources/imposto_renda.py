
from libs import calculos
from flask_smorest import Blueprint
from flask import jsonify
from flask.views import MethodView

from schema import IrSchema, InssSchema

blp = Blueprint("Calculadoras", "calculadoras", description="Calculadoras para Imposto de Renda e INSS")





@blp.route("/imposto_renda")
class imposto_renda(MethodView):
    @blp.arguments(IrSchema)
    @blp.response(200)
    def post(self, renda_data):
        """Recebe o salario, os dependentes, as despesas
        em educação, saúde, pensão, previdência e doações 
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
        return {"imposto_de_renda " : ir, "INSS": inss,
                "salario": salario, "deducao" : deducao,
                "dependentes": dependentes}
        
    @blp.response(200)
    def get(self):
        
        return {
            "Imposto_de_renda":
                    "Para calcular o imposto de renda, informe o valor mensal do salario,\
                         os dependentes e as despesas em educação, saúde, pensão, previdência\
                            e doações ",
            "INSS": 
                    "Para calcular o INSS, informe o valor mensal do salario"}
        
@blp.route("/inss")
class INSS(MethodView):
    @blp.arguments(InssSchema)
    @blp.response(200)
    def post(self, renda_data):
        salario = renda_data['salario']
        inss = round(calculos.inss(salario),2)
        return {"INSS": f"R${inss}/por mês"}