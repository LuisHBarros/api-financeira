Uma API simples para finanças, construída com Python, flask, flask-smorest e Swagger ( para a auto-documentação da API)

Deploy feito na EC2 da AWS, com Docker e Docker-Compose

Contem consultas sobre algumas moedas e criptomoedas, dados sobre ações no dia (maiores altas e baixas, etc...), além de calculadoras de imposto de renda e INSS.

Boa parte da API funciona via 'Web scrapping', tanto para informar o valor das moedas disponíveis, quanto para informar dados sobre as ações do dia

Já as calculadoras, são cálculos básicos feitos por meio de dados informados pelo cliente para a API ( como salário, gasto com educação, dependentes, etc...)

O projeto conta com um docker-compose básico, apenas para rodar o python e executar o comando 'flask run'

Link para a API : http://15.228.237.165:5000/swagger-ui
