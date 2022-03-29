from xml.sax import default_parser_list
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

def get_crypto():

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

    crypto_list = {}
    
    for i in range(len(data['data'])):
      details = {}
          
      details['symbol'] = data['data'][i]['symbol']
      details['price'] = round(data['data'][i]['quote']['EUR']['price'], 2)
      details['percent_change'] = data['data'][i]['quote']['EUR']['percent_change_24h']
      
      crypto_list[data['data'][i]['name']] = details
          
    return crypto_list
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    pprint(e)

if __name__ == "__main__":
    get_crypto()


# url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
# parameters = { 
#   'convert': 'EUR',
#   'limit': 20
# }
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': '5fc07844-7ff1-4e9e-805c-d57906b1ce07',
# }

# session = Session()
# session.headers.update(headers)

# try:
#   response = session.get(url, params=parameters)
#   data = json.loads(response.text)
  
#   with open("app/list_crypto.json", "r") as f:
#     crypto_list = json.load(f)
  
#   for i in range(len(data['data'])):
#     details = {}
        
#     details['symbol'] = data['data'][i]['symbol']
#     details['price'] = round(data['data'][i]['quote']['EUR']['price'], 2)
#     details['percent_change'] = data['data'][i]['quote']['EUR']['percent_change_24h']
#     details['quantity'] = 0
    
    
#     crypto_list[data['data'][i]['name']] = details
    
#   with open("list_crypto.json", "w") as f:
#     json.dump(crypto_list, f, indent=4)
    
#   # pprint(crypto_list)
  
#   # return crypto_list

# except (ConnectionError, Timeout, TooManyRedirects) as e:
#   pprint(e)