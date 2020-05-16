import random
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime

def resMoned(nombremone,CantMone,preciomon):
    print(nombremone.upper())
    print("En este momento usted possee: ",CantMone[nombremone],nombremone.upper())
    print("Equivalente a: ,",str(CantMone[nombremone]*preciomon[nombremone]),"USD")


def is_int(dat):
    try: 
        int(dat)
        return True
    except:
        print("Error: ingrese un numero entero")
        return False

def printMat(lis):
    for i in lis:
        for j in i:
            print(j,end='\t\t')
            print('')

def monedasDict():
    opcionMonedas = ["BTC","ETH","XRP","BCH","LTC","EOS","BNB","XTZ"]
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '7dc3eb05-b9ca-401e-835e-1eaceaef62cf',
    }

    session = Session()
    session.headers.update(headers)
    moneda_dict = {}

    




