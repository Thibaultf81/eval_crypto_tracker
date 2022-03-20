from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from pprint import pprint

def get_crypto():

  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC,ETH'
  parameters = { 
    'convert': 'EUR'
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
    return data
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    pprint(e)

if __name__ == "__main__":
    get_crypto()