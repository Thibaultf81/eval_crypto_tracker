from flask import Flask, render_template
# from pprint import pprint


total_invests = 5000

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        from app.api import get_crypto
        data = get_crypto()
        
        btc_symbol = list(data['data'])[0]
        btc_name = data['data']['BTC']['name']
        eth_symbol = list(data['data'])[1]
        eth_name = data['data']['ETH']['name']

        return render_template('index.html', btc_name = btc_name,
                               btc_symbol = btc_symbol,
                               eth_symbol = eth_symbol,
                               eth_name = eth_name,
                               total_invests = total_invests)

    @app.route('/about/')
    def about():
        return 'This is the about page'

    return app