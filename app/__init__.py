from flask import Flask, render_template, request
import json

from pprint import pprint

# On récupère la base de données json que l'on instance avec la variable "crypto_list"
with open("app/list_crypto.json", "r") as f:
    crypto_list = json.load(f)

# def create_app():
app = Flask(__name__)

@app.route('/')
def homepage():

    return render_template('index.html', crypto_list=crypto_list)

@app.route('/achat/', methods=["POST", "GET"])
def buyPage():
    
    return render_template('achat.html', crypto_list=crypto_list)

if __name__ == '__main__':
    app.run(debug=True)
        



    # @app.route('/vente/', methods=["POST", "GET"])
    # def sell():
        
    #     return render_template('vente.html', cryptos=list_cryptos)


    # return app

