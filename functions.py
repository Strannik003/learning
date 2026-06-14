import json
import datetime
import os
import random
from pathlib import Path

operacje = []
balans = 0

def add_doch(x):
    global balans
    czas = datetime.datetime.now()
    operacja = {
        "Day": czas.strftime("%d/%m/%Y"),
        "suma_trans":int(x),
        "kategoria": "Dochod"
    }
    balans += int(x)
    operacje.append(operacja)
    return operacje
def add_rozch(x,y):
    global balans
    czas = datetime.datetime.now()
    operacja = {
        "Day": czas.strftime("%d/%m/%Y"),
        "suma_trans": -int(x),
        "kategoria": y
    }
    balans +=int(x)
    operacje.append(operacja)
    return operacje

def show_operations():
    for operacja in operacje:
        print(f"{operacja['Day']} | {operacja['kategoria']} | {operacja['suma_trans']}")
    
def balansik():
    print(f'Твой баланс сейчас : {balans}')

def rasch_po_kat():
    result = {}

    for operacja in operacje:
        if operacja["suma_trans"] < 0:
            kategoria = operacja["kategoria"]
            suma = operacja["suma_trans"]

            if kategoria not in result:
                result[kategoria] = 0

            result[kategoria] += suma

    print("\nРасходы по категориям:")

    for kategoria, suma in result.items():
        print(f"{kategoria}: {suma}")


def today_operations():
    result = []
    czas = datetime.datetime.now()
    for operacja in operacje:
        if  operacja["day"] == czas.strftime("%d/%m/%Y"):
            print(f" {operacja['kategoria']} | {operacja['suma_trans']}")