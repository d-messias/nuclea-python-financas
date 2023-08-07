import re


def tickerValidator():
    validatedTicker = r'^[A-Z]{4}\d{1}$'

    while True:
        ticker = input("TICKER: ").upper()

        if re.match(validatedTicker, ticker):
            return ticker
        else:
            print("TICKER inválido! Tente novamente: ")
