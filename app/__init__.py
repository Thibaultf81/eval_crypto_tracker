from flask import Flask, render_template, request
# from pprint import pprint

from app.api import get_crypto
crypto_list = get_crypto()

BTC_invest = 3000
ETH_invest = 2000

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():

        return render_template('index.html', crypto_list=crypto_list)

    @app.route('/achat/', methods=["POST", "GET"])
    def buy():
        
        return render_template('achat.html', crypto_list=crypto_list)


    # @app.route('/vente/', methods=["POST", "GET"])
    # def sell():
        
    #     return render_template('vente.html', cryptos=list_cryptos)


    return app

