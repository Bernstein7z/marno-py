import requests


def get_location() -> dict:
    url = 'http://ip-api.com/json/?fields=8404995'
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None


def get_current_silver_price() -> dict:
    location = get_location()
    metal = 'XAG'  # silver
    url = f'https://www.goldapi.io/api/{metal}/{location["currency"]}'
    headers = {
        'x-access-token': 'goldapi-qpbyhykd2c5bks-io',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers).json()
    return {'price': response['price'], 'currency': location['currency']}


def calc() -> dict:
    silver = get_current_silver_price()
    nokhod = 0.192
    gheran = 24 * nokhod
    shahi = gheran / 10
    messqhal_sirfi = 4.608
    silver_gram_price = float(silver["price"]) / 28.34952  # 1 ounce = 28.34952 g

    sar_fetr = (1 / 4) * messqhal_sirfi * silver_gram_price
    sarane = 3 * messqhal_sirfi * silver_gram_price
    teymur = shahi * silver_gram_price

    return {
        'sarfetr': round(sar_fetr, 2),
        'sarane': round(sarane, 2),
        'teymur': round(teymur, 2)
    }


def print_results():
    pass


print_results()

# TODO: get references for calculations
# TODO: tests
# TODO: khedmat, gerde
# TODO: family member amount
