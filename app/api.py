from xml.sax import default_parser_list
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

def get_crypto():
  
  # L'appel de l'API a été directement récupéré dans la documentation de l'API CoinMarketCap
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = { 
    'convert': 'EUR',
    'limit': 20
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '5fc07844-7ff1-4e9e-805c-d57906b1ce07',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)

    # Je crée un dictionnaire vide
    crypto_list = {}
    
    # Pour chaque crypto présent dans le résultat de l'appel de l'API (en l'occurence 20)
    # Je rajoute une clé correspondant à une crypto, et en valeurs un dictionnaire avec le symbole, le prix et le taux de change
    for i in range(len(data['data'])):
      details = {}
          
      details['symbol'] = data['data'][i]['symbol']
      details['price'] = round(data['data'][i]['quote']['EUR']['price'], 2)
      details['percent_change'] = data['data'][i]['quote']['EUR']['percent_change_24h']
      
      crypto_list[data['data'][i]['name']] = details
       
    # Je retourne ainsi le dictionnaire avec toutes les informations ci-dessus   
    return crypto_list
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    pprint(e)

if __name__ == "__main__":
    get_crypto()
