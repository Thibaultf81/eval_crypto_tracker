from flask import Flask, render_template, request
import json

from pprint import pprint

import app.api
crypto_list = api.get_crypto()

# def create_app():
app = Flask(__name__)

# initialisation de la page d'accueil de l'application
@app.route('/')
def homepage():

    return render_template('index.html', crypto_list=crypto_list)


# On génère le chemin menant à la page permettant d'acheter une cryptomonnaie
@app.route('/achat/', methods=["POST", "GET"])
def buyPage():
    
    # # On récupère la base de données json que l'on instancie avec la variable "crypto_list"
    # with open("app/list_crypto.json", "r") as f:
    #     crypto_list = json.load(f)
    
    # # On récupère la crypto choisie avec la quantité voulu, et on ajoute cette quantité à la crypto en question
    # if request.method == 'POST':
    #     crypto = request.form['select_crypto']
    #     quantity = request.form['quantity_crypto']
    #     crypto_list[crypto]['quantity'] += float(quantity)
    
    # # On écrase la base de données avec la quantité que l'on a ajouté à la crypto choisie
    # with open("app/list_crypto.json", "w") as f:
    #     json.dump(crypto_list, f, indent=4)
    
    return render_template('achat.html', crypto_list=crypto_list)


if __name__ == '__main__':
    app.run(debug=True)
        



    # @app.route('/vente/', methods=["POST", "GET"])
    # def sell():
        
    #     return render_template('vente.html', cryptos=list_cryptos)


    # return app

