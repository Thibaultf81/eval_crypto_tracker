from flask import Flask, render_template
from pprint import pprint

crypto1 = "Bitcoin"
crypto2 = "Ethereum"



def create_app():
    app = Flask(__name__)

    

    @app.route('/')
    def homepage():
        from app.api import get_crypto
        data = get_crypto()

        return render_template('index.html', crypto1 = data['data']['BTC']['name'], crypto2 = data['data']['ETH']['name'])

    @app.route('/about/')
    def about():
        return 'This is the about page'

    

    return app