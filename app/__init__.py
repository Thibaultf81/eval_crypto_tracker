from flask import Flask, render_template, request
import json

from pprint import pprint

# On importe la fonction permettant de récupérer les informations de l'API CoinMarketCap
from app import api
crypto_list = api.get_crypto()

# def create_app():
app = Flask(__name__)

# initialisation de la page d'accueil de l'application
@app.route('/')
def homepage():
    
    # On récupère la base de données JSON en mode lecture
    with open("app/wallet_crypto.json", "r") as f:
        wallet_crypto = json.load(f)
        
    # On calcule le montant total investi dans les cryptomonnaies et la plus_value totale
    total_invests = 0
    win_loss = 0
    for crypto in wallet_crypto:
        total_invests += wallet_crypto[crypto]['total_price']
        win_loss += round(wallet_crypto[crypto]['total_price'] * (crypto_list[crypto]['percent_change'] / 100), 2)

    return render_template('index.html', crypto_list=crypto_list,
                                        total_invests=total_invests,
                                        win_loss=win_loss)


# On génère le chemin menant à la page permettant d'acheter une cryptomonnaie
@app.route('/achat/', methods=["POST", "GET"])
def buyPage():
    
    # On ouvre la base de données JSON où l'on va indiquer la quantité de cryptomonnaies de notre portefeuille
    with open("app/wallet_crypto.json", "r") as f:
        wallet_crypto = json.load(f)
    
    # On récupère du formulaire la crypto choisie, le prix d'achat ainsi que la quantité voulue et on ajoute ces informations dans la base de données
    if request.method == 'POST':
        
        crypto = request.form['select_crypto']
        quantity = float(request.form['quantity_crypto'])
        total_price = round(float(request.form['price']), 2) * quantity
        
        if crypto in wallet_crypto.keys():
            wallet_crypto[crypto]['quantity'] += quantity
            wallet_crypto[crypto]['total_price'] += total_price
        else:
            wallet_crypto[crypto] = {}
            wallet_crypto[crypto]['quantity'] = quantity
            wallet_crypto[crypto]['total_price'] = total_price
        
        # print(price)
        
    
    # On écrase la base de données avec la quantité que l'on a ajouté à la crypto choisie
    with open("app/wallet_crypto.json", "w") as f:
        json.dump(wallet_crypto, f, indent=4)
    
    # On affiche la page achat.html en indiquant le résultat de l'appel de l'API pour afficher la liste des cryptomonnaies et de leur prix
    return render_template('achat.html', crypto_list=crypto_list)


if __name__ == '__main__':
    app.run(debug=True)
        



    # @app.route('/vente/', methods=["POST", "GET"])
    # def sell():
        
    #     return render_template('vente.html', cryptos=list_cryptos)


    # return app

