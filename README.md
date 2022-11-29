Uma API simples para finanças, construida com Python, flask, flasksmorest e Swagger ( para a autodocumentacao da API)

Contem consultas sobre algumas moedas e criptomoedas, dados sobre ações no dia (maiores altas e baixas, etc...), além de calculadoras de imposto de renda e INSS.

Boa parte da API funciona via 'Web scrapping', tanto para informar o valor das moedas disponíveis, quanto para informar dados sobre as ações do dia
 
Já as calculadoras, são calculos básicos feitos por meio de dados informados pelo cliente para a API ( como salário, gasto com educação, dependentes, etc...)

O projeto conta com um docker-compose básico, apenas para rodar o python e executar o comando 'flask run'
