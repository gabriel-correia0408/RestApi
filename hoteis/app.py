#Fazendo o chamado da biblioteca flask e importando de dentro dela o "Flask"
from flask import Flask

#chamandoa biblioteca flask_restful e importando dela "Resource", e "Api"
from flask_restful import Resource, Api

#criando uma variavél por padrão "app", e vamos passar o flask para ela junto de f(__name__)
app = Flask(__name__)
#criando agora uma variavél para Api
api = Api(app)

#criando uma classe hoteis
# Esta primeira classe leva em seus (), Resource porque vai ser um recurso da nossa Api
# este recurso como todos os recursos devem, conter Get Post e Delete
# e o Api que foi instanciado é quem vai fazer o gerenciamento de toda a aplicação
class Hoteis(Resource):
    def get(self):
        # aqui está sendo feito um dicionário,porém quando for feito a requisição, a biblioteca
        #flask_restful, vai retornar automaticamente nos retornar em formato json
        return {'hoteis': 'meus hoteis'}



api.add_resource(Hoteis, '/hoteis')


if __name__ == '__main__':
    app.run(debug=True)
