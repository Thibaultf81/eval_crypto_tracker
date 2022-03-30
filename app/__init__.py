from flask import Flask, render_template, request
import json
from emoji import emojize

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
        total_invests += round(wallet_crypto[crypto]['total_price'], 2)
        win_loss += round(wallet_crypto[crypto]['total_price'] * (crypto_list[crypto]['percent_change'] / 100), 2)

    # On renvoie la page d'accueil contenue dans le fichier index.html, et on fait correspondre la variables appelée grâce à Jinja2
    return render_template('index.html', crypto_list=crypto_list,
                                        total_invests=total_invests,
                                        win_loss=win_loss,
                                        wallet_crypto=wallet_crypto)


# On génère le chemin menant à la page permettant d'acheter une cryptomonnaie
@app.route('/achat/', methods=["POST", "GET"])
def buyPage():
    
    # On ouvre la base de données JSON que l'on intègre dans une variable
    with open("app/wallet_crypto.json", "r") as f:
        wallet_crypto = json.load(f)
    
    # On récupère du formulaire la crypto choisie, le prix d'achat ainsi que la quantité voulue et on ajoute ces informations dans la base de données
    if request.method == 'POST':
        
        # On récupère les données du formulaire
        crypto = request.form['select_crypto']
        quantity = float(request.form['quantity_crypto'])
        total_price = round(float(request.form['price']), 2) * quantity
        
        # Si la crypto se trouve dans la base de données, on ajoute la quantité définie et on modifie le total investi
        if crypto in wallet_crypto.keys():
            wallet_crypto[crypto]['quantity'] += quantity
            wallet_crypto[crypto]['total_price'] += total_price
        # Si la crypto ne se trouve pas dans la base, on l'ajoute avec les informations définie
        else:
            wallet_crypto[crypto] = {}
            wallet_crypto[crypto]['quantity'] = quantity
            wallet_crypto[crypto]['total_price'] = total_price
    
    # On écrase la base de données avec la quantité que l'on a ajouté à la crypto choisie
    with open("app/wallet_crypto.json", "w") as f:
        json.dump(wallet_crypto, f, indent=4)
    
    # On affiche la page achat.html en indiquant le résultat de l'appel de l'API pour afficher la liste des cryptomonnaies et de leur prix
    return render_template('achat.html', crypto_list=crypto_list)


if __name__ == '__main__':
    app.run(debug=True)
        



@app.route('/vente/', methods=["POST", "GET"])
def sell():
    
    # On ouvre la base de données JSON que l'on intègre dans une variable
    with open("app/wallet_crypto.json", "r") as f:
        wallet_crypto = json.load(f)
    
    if request.method == 'POST':
        
        # On récupère les données du formulaire
        crypto = request.form['select_crypto']
        quantity = float(request.form['quantity_crypto'])
        
        # Si la crypto se trouve dans la base de données, on enlève la quantité de crypto définie dans le formulaire, ainsi que le total investi
        if crypto in wallet_crypto.keys():
            wallet_crypto[crypto]['quantity'] -= quantity
            wallet_crypto[crypto]['total_price'] -= quantity * crypto_list[crypto]['price']
           
        # Si la quantité d'une crypto est égale à 0, on la supprime de la base de données 
        if wallet_crypto[crypto]['quantity'] <= 0:
            wallet_crypto.pop(crypto)
    
    # On écrase la base de données avec les informations ci-dessus
    with open("app/wallet_crypto.json", "w") as f:
        json.dump(wallet_crypto, f, indent=4)
    
    # On affiche la page vente.html
    return render_template('vente.html', crypto_list=crypto_list)


