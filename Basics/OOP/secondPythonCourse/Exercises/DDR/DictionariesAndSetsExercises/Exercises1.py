def addCurrency(currency):
    currency['India'] = "Rupee"
    currency['UK'] = 'Pound'
    currency['Japan'] = 'Yen'
    currency['Austria'] = 'Euro'
    currency['Bangladesh'] = 'Taka'
    return currency


def deleteCurrency(currency):
    del currency['UK']
    print(currency)


def deleteJapan(currency):
    c = currency.pop("Japan")
    return c


def deleteRandomKeyValue(currency):
    currency.popitem()


def newEntryToDictionary(currency):
    currency["Switzerland"] = "Swiss Franc"


def changeIndiaValue(currency):
    currency["India"] = "Indian Rupee"


def showEverything(currency):
    print(currency.keys())
    print(currency.values())
    print(currency.items())


def fruitDictionary(fruits_prices):
    print(fruits_prices["apple"])
    fruits_prices["grapes"] = 0


def main():
    currency = {}
    fruits_prices = {
        "apple": 100,
        "banana": 75,
        "mango": 80
    }

    print(addCurrency(currency))
    print()
    deleteCurrency(currency)
    print()
    print(deleteJapan(currency))
    print()
    deleteRandomKeyValue(currency)
    print(currency)
    print()
    newEntryToDictionary(currency)
    print(currency)
    print()
    changeIndiaValue(currency)
    print()
    print(currency)
    print()
    print(showEverything(currency))
    print()
    fruitDictionary(fruits_prices)
    print(fruits_prices)
    print()


main()
