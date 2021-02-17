import requests


def get_latest_trading_prices(currencies):

    for currency in currencies:

        query = {'command': 'returnTradeHistory', 'currencyPair': currency}

        r = requests.get('https://poloniex.com/public', params=query)

        # raise an exception in case there was an error
        r.raise_for_status()

        print(f"{currency} : {r.json()[0]['rate']}")

# get_latest_trading_prices(['BTC_ETH', 'BTC_ETC'])    

def get_latest_trading_prices():

    r = requests.get('https://poloniex.com/public?command=returnTicker')

    # raise an exception in case there was an error
    r.raise_for_status()

    for currency in r.json():
        print(f"{currency} : {r.json()[currency]['last']}")

get_latest_trading_prices()