VALOR_DEPENDENTES = 189.59

VALOR_EDUCACAO = 3561.50

INSS_FAIXA1_VALOR = 1212.00
INSS_FAIXA1_TAXA = 0.075
INSS_FAIXA2_VALOR = 2427.35
INSS_FAIXA2_TAXA = 0.09
INSS_FAIXA3_VALOR = 3641.03
INSS_FAIXA3_TAXA = 0.12
INSS_FAIXA4_VALOR = 7087.22
INSS_FAIXA4_TAXA = 0.14
INSS_FAIXA5_VALOR = 0


IR_FAIXA1_VALOR = 1903.98
IR_FAIXA1_TAXA = 0.00
IR_FAIXA2_VALOR = 2826.65
IR_FAIXA2_TAXA = 0.075
IR_FAIXA3_VALOR = 3751.06
IR_FAIXA3_TAXA = 0.15
IR_FAIXA4_VALOR = 4664.68
IR_FAIXA4_TAXA = 0.225
IR_FAIXA5_VALOR = 0
IR_FAIXA5_TAXA = 0.275



def dependentes(dependentes):
    return dependentes* VALOR_DEPENDENTES


def educacao(educacao, dependentes):
    if educacao > dependentes * VALOR_EDUCACAO:
        return dependentes * VALOR_EDUCACAO
    else:
        return educacao
    
def inss(salario):
    if salario < INSS_FAIXA1_VALOR:
        return ((salario * INSS_FAIXA1_TAXA))
    if salario < INSS_FAIXA2_VALOR:
        primeira_faixa = INSS_FAIXA1_VALOR * INSS_FAIXA1_TAXA
        return ((salario - INSS_FAIXA1_VALOR) * INSS_FAIXA2_TAXA) + primeira_faixa
    if salario < INSS_FAIXA3_VALOR:
        primeira_faixa = INSS_FAIXA1_VALOR * INSS_FAIXA1_TAXA
        segunda_faixa = (INSS_FAIXA2_VALOR - INSS_FAIXA1_VALOR) * INSS_FAIXA2_TAXA
        return ((salario - INSS_FAIXA2_VALOR) * INSS_FAIXA3_TAXA) + primeira_faixa + segunda_faixa
    if salario < INSS_FAIXA4_VALOR:
        primeira_faixa = INSS_FAIXA1_VALOR * INSS_FAIXA1_TAXA
        segunda_faixa = (INSS_FAIXA2_VALOR - INSS_FAIXA1_VALOR) * INSS_FAIXA2_TAXA
        terceira_faixa = (INSS_FAIXA3_VALOR - INSS_FAIXA2_VALOR) * INSS_FAIXA3_TAXA
        return (((salario - INSS_FAIXA3_VALOR)) * INSS_FAIXA4_TAXA) + primeira_faixa + segunda_faixa + terceira_faixa
    #Salario > INSS_FAIXA4_VALOR
    primeira_faixa = INSS_FAIXA1_VALOR * INSS_FAIXA1_TAXA
    segunda_faixa = (INSS_FAIXA2_VALOR - INSS_FAIXA1_VALOR) * INSS_FAIXA2_TAXA
    terceira_faixa = (INSS_FAIXA3_VALOR - INSS_FAIXA2_VALOR) * INSS_FAIXA3_TAXA
    quarta_faixa = (INSS_FAIXA4_VALOR - INSS_FAIXA3_VALOR) * INSS_FAIXA4_TAXA
    return primeira_faixa + segunda_faixa + terceira_faixa + quarta_faixa

def imposto_renda(salario, dependentes, inss, deducao):
    total = (salario - dependentes - inss)
    if total < IR_FAIXA1_VALOR: #Faixa de isencao
        print(total)
        return 0
    if total < IR_FAIXA2_VALOR:
        return ((total - IR_FAIXA1_VALOR) * IR_FAIXA1_TAXA - deducao)
    if total < IR_FAIXA3_VALOR:
        primeira_faixa = (IR_FAIXA2_VALOR - IR_FAIXA1_VALOR) * IR_FAIXA1_TAXA
        print(primeira_faixa)
        return (((total - IR_FAIXA3_VALOR) * IR_FAIXA3_TAXA) + primeira_faixa) - deducao
    if total < IR_FAIXA4_VALOR:
        primeira_faixa = (IR_FAIXA2_VALOR - IR_FAIXA1_VALOR) * IR_FAIXA1_TAXA
        print(primeira_faixa)
        segunda_faixa = (IR_FAIXA3_VALOR - IR_FAIXA2_VALOR) * IR_FAIXA3_TAXA
        print("segunda_faixa")
        return (((total - IR_FAIXA3_VALOR) * IR_FAIXA4_TAXA) + primeira_faixa + segunda_faixa) - deducao
    primeira_faixa = (IR_FAIXA2_VALOR - IR_FAIXA1_VALOR) * IR_FAIXA1_TAXA #961.67
    print(primeira_faixa)
    segunda_faixa = (IR_FAIXA3_VALOR - IR_FAIXA2_VALOR) * IR_FAIXA3_TAXA
    print(segunda_faixa)
    terceira_faixa = (IR_FAIXA4_VALOR - IR_FAIXA3_VALOR) * IR_FAIXA4_TAXA
    print(terceira_faixa)
    return (((total - IR_FAIXA4_VALOR) * IR_FAIXA5_TAXA) + primeira_faixa + segunda_faixa + terceira_faixa) - deducao
