import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = 'FTQ9WHQ00JGQCWVI'
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    return float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    return amount * exchange_rate

# Obtener el valor del euro en pesos argentinos
euro_to_ars = get_exchange_rate('ARS', 'EUR')

# Obtener el valor del dólar oficial en pesos argentinos
usd_to_ars = get_exchange_rate('ARS', 'EUR')

# Ejemplo de conversión de pesos argentinos a euros
amount_ars = 1
converted_amount_eur = convert_currency(amount_ars, 'EUR', 'ARS')
print(f'{amount_ars} pesos argentinos equivalen a {converted_amount_eur:.2f} euros')

# Ejemplo de conversión de pesos argentinos a dólares
amount_ars = 1
converted_amount_usd = convert_currency(amount_ars, 'USD', 'ARS')
print(f'{amount_ars} pesos argentinos equivalen a {converted_amount_usd:.2f} dólares')
