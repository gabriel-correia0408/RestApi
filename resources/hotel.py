from flask_restful import Resource


#criando uma lista de hoteis para ser usada em nossa aplicação Api
#logo a meta é trazer está lista de um banco de  dados ,ao invés de formato json,como é
# oque estou fazendo.
hoteis = [
    {
        'hotel_id': 'alpha',
        'nome': 'Alpha Hotel',
        'estrela': 4.3,
        'diaria': 420.34,
        'cidade': 'Curitiba'
    },

    {
        'hotel_id': 'charlie',
        'nome': 'Charlie Hotel',
        'estrela': 4.4,
        'diaria': 380,
        'cidade': 'Florianópolis'
    },

    {
        'hotel_id': 'bravo',
        'nome': 'Bravo Hotel',
        'estrela': 4.0,
        'diaria': 390,
        'cidade': 'Porto Alegre'
    }
]
#criando uma classe hoteis
# Esta primeira classe leva em seus (), Resource porque vai ser um recurso da nossa Api
# este recurso como todos os recursos devem, conter Get Post e Delete
# e o Api que foi instanciado é quem vai fazer o gerenciamento de toda a aplicação
class Hoteis(Resource):
    def get(self):
        # aqui está sendo feito um dicionário,porém quando for feito a requisição, a biblioteca
        #flask_restful, vai retornar automaticamente nos retornar em formato json
        return {'hoteis': hoteis}