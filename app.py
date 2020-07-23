from flask import Flask

from resources.hotel import Hoteis, Hotel

from flask_restful import Api

# criando uma variavél por padrão "app", e vamos passar o flask para ela junto de (__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# criando agora uma variavél para api, para instanciar a "Api"
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

api.add_resource(Hoteis, '/hoteis')
# criando um novo endpoint , por ser uma string ,vai na formatação abaixo <string....>
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)