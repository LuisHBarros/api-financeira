
from libs import calculos
from flask_smorest import Blueprint
from flask import jsonify
from flask.views import MethodView

from schema import IrSchema

blp = Blueprint("Imposto_renda", "imposto_de_renda", description="Calcula o imposto de renda")





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
        return {"imposto de renda " : ir, "INSS": inss,
                "salario": salario, "deducao" : deducao,
                "dependentes": dependentes}
        
    @blp.response(200)
    def get(self):
        
        return {"message": 
            ("Para calcular o imposto de renda, informe o valor do salario, os dependentes e as despesas em educação, saúde, pensão, previdência e doações ")}
        
    