#Fazendo o chamado da biblioteca flask e importando de dentro dela o "Flask"
from flask import Flask
# Agora chamando a pasta resources que nela esta o arquivo "hoteis" ,e fazemos a importação
# da classe Hoteis, assim fazemos uma pequena fatoração ,para comparação do código anteriormente
# sendo uma divisão em pacote. Desta maneira deixando o código mais organizado
from resources.hotel import Hoteis

#chamandoa biblioteca flask_restful e importando dela "Resource", e "Api"
from flask_restful import  Api

#criando uma variavél por padrão "app", e vamos passar o flask para ela junto de (__name__)
app = Flask(__name__)
#criando agora uma variavél para api, para instanciar a "Api"
api = Api(app)

api.add_resource(Hoteis, '/hoteis')

if __name__ == '__main__':
    app.run(debug=True)
