import requests


def get_latest_trading_prices(currencies):

    for currency in currencies:

        query = {'command': 'returnTradeHistory', 'currencyPair': currency}

        r = requests.get('https://poloniex.com/public', params=query)
        r.raise_for_status()

        print(f"{currency} : {r.json()[0]['rate']}")

get_latest_trading_prices(['BTC_ETH', 'BTC_ETC'])    