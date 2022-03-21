from flask import Flask, render_template, request
# from pprint import pprint

from app.api import get_crypto
data = get_crypto()

BTC_percent_change = data['data']['BTC']['quote']['EUR']['percent_change_24h']
ETH_percent_change = data['data']['ETH']['quote']['EUR']['percent_change_24h']
BTC_price = data['data']['BTC']['quote']['EUR']['price']
ETH_price = data['data']['ETH']['quote']['EUR']['price']

BTC_invest = 3000
ETH_invest = 2000

win_loss = round((BTC_invest * (BTC_percent_change / 100)) + (ETH_invest * (ETH_percent_change / 100)),2)

total_invests = BTC_invest + ETH_invest + win_loss

btc_symbol = list(data['data'])[0]
btc_name = data['data']['BTC']['name']
eth_symbol = list(data['data'])[1]
eth_name = data['data']['ETH']['name']

list_cryptos = [
                {"crypto": btc_name, "price": round(BTC_price, 2)},
                {"crypto": eth_name, "price": round(ETH_price, 2)}
            ]

if win_loss >= 0:
    symbol_win_loss = "+"
else:
    symbol_win_loss = ""

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():

        return render_template('index.html', btc_name = btc_name,
                               btc_symbol = btc_symbol,
                               eth_symbol = eth_symbol,
                               eth_name = eth_name,
                               total_invests = total_invests,
                               win_loss = win_loss,
                               symbol_win_loss = symbol_win_loss,
                               BTC_invest = BTC_invest,
                               ETH_invest = ETH_invest)

    @app.route('/achat/', methods=["POST", "GET"])
    def buy():
        
        return render_template('achat.html', cryptos=list_cryptos)


    @app.route('/vente/', methods=["POST", "GET"])
    def sell():
        
        return render_template('vente.html', cryptos=list_cryptos)


    return app


    return app

