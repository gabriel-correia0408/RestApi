from flask_restful import Resource, reqparse


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
# Esta primeira classe leva em seus (), Resource porque vai ser um recurso da Api
# este recurso como todos os recursos devem, conter Get Post e Delete
# e o Api que foi instanciado é quem vai fazer o gerenciamento de toda a aplicação
class Hoteis(Resource):
    def get(self):
        # aqui está sendo feito um dicionário,porém quando for feito a requisição, a biblioteca
        #flask_restful, vai retornar automaticamente nos retornar em formato json
        return {'hoteis': hoteis}

#criando mais classe para o app, como está classe também vai ser um recurso ela ,herda da biblioteca restfull, c classe
# Resource
class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'Hotel not found.'}, 404 # not found

    def post(self, hotel_id):
        # nas linhas abaixo será criado um construtor
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_argument('diaria')
        argumentos.add_argument('cidade')
        # a variavél dados vai ser ,estilo chave e valor que deverá ser passado, sendo um construtor
        dados = argumentos.parse_args()
        #dados a serem recebidos
        novo_hotel = {
            'hotel_id': hotel_id,
            'nome': dados['nome'],
            'estrelas': dados['estrelas'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']

        }
        #agora adicionando o novo elemento na lista através do método de adiconar append assim adicionando o elemento
        # "novo_hotel "
        hoteis.append(novo_hotel)
        #retornando a variavél que contém os dados , e o código 200 que é codigo indicando sucesso
        return novo_hotel, 200

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass