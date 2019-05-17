import requests
import json
import time
import sys


class Rate:
    def __init__(self, eur, time):
        self.eur = eur
        self.time = time

    def __str__(self):
        return "Time: " + self.time + "\nRate: " + self.eur + " [EUR]"


TICKER_URL = "https://api.coindesk.com/v1/bpi/currentprice.json"
def get_rate():
    try:
        r = requests.get(TICKER_URL)
    except Exception as ex:
        raise ex
    res = r.json()
    return Rate( res["bpi"]["EUR"]["rate"] , res["time"]["updated"])



BALANCE_URL = "https://blockchain.info/q/addressbalance/"
def get_balance(addr):
    try:
        r = requests.get(BALANCE_URL + str(addr) + "?confirmations=6")
    except Exception as ex:
        raise ex
    print(r.text)
    print(r.text)
    return int(r.text)


def main():
    rate = 0
    try:
        rate = get_rate()
    except Exception as ex:
        print("unable to get bitcoin rate | " + ex)
        return

    print(str(rate))

    if len(sys.argv) <= 1:
        return

    addr = sys.argv[1]
    print("Requesting Balance of: " + addr)

    balance = 0
    try:
        balance = get_balance(addr)
    except Exception as ex:
        print("unable to get balance | " + ex);
        return


    str_rate = []
    for c in rate.eur:
        if c != ",":
            str_rate.append(c)

    print("-- Address Balance --")
    print(" - " + str(balance / 100000000))
    print(" - " + str(balance) + " [Sat]")
    print(" - " + str((balance / 100000000) * float("".join(str_rate))) + " [Eur]")


if __name__ == "__main__":
    main()
