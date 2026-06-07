# 1. Добавить доход
# 2. Добавить расход
# 3. Показать все операции
# 4. Показать баланс
# 5. Показать расходы по категориям
# 6. Показать операции за сегодня
# 7. Выйти



import json
import datetime
import os
import random
from pathlib import Path

operacje = []
kat_rachodov = ["Общие","Стриптиз","Массажка"]
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



if __name__ == '__main__':
    while True:
            print("\nМеню:")
            print("1. Добавить доход")
            print("2. Добавить расход")
            print("3. Покажи операции")
            print("4. Покажи баланс")
            print("5. Покажи расход по категориям")
            print("6. Покажи операции за сегодня")
            print("7. Выйти")

            choice = input("Выбери действие: ")

            match choice:
                case "1":
                    dochod = input("Сколь пришло от родителей на пирожки : ")
                    add_doch(dochod)

                case "2":
                    razchod = input("Сколь потратил ")
                    print ("\nКатегории:")
                    print("1. Общие")
                    print("2. Стриптиз")
                    print("3. Массажка")
                    choice2 = input("Выбери категорию: ")
                    if choice2 == "1":
                        add_rozch(razchod,"Общие")
                    if choice2 == "2":
                        add_rozch(razchod,"Стриптиз")
                    else:
                        add_rozch(razchod,"Массажка")

                case "3":
                    show_operations()

                case "4":
                    balansik()
                
                case "5":
                    rasch_po_kat()

                case "6":
                    today_operations()
                
                case "7":
                    break
                
                case _:
                    print("Такого пункта нет")



                


