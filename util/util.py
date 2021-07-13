import hashlib
import urllib
import json
from decimal import Decimal

def hashPersonList(list):
    for person in list:
        toHash = person['first_name'] + person['second_name'] + person['birth_date']
        encoded = toHash.encode()
        person['hash'] = hashlib.sha256(encoded).hexdigest()
    return

def getJSONFromURL(string):
    response = urllib.request.urlopen(string)
    data = json.loads(response.read())
    return data

def calcBTCPrice(amount, orderbook):
    totalPrice = 0
    amount = float(amount)
    if amount == 0:
        return 0
    if amount < 0:
        raise Exception('Cannot buy negative amount of Bitcoin')
    for offer in orderbook:
        print(amount)
        restToBuy = amount
        amount -= offer[1]
        if amount <= 0:
            totalPrice += offer[0]*restToBuy
            break
        else:
            totalPrice += offer[0]*offer[1]
    return round(totalPrice,2)
