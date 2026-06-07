
# Программа “Дневник”, которая сохраняет записи с датой и временем.

import datetime 
cashe_perm = []
cache_is_valid = False


def add_note(tekst):
    with open("Diary.txt", "a", encoding="utf-8") as file1:
        x = datetime.datetime.now()
        file1.write(f'{x} : {tekst}\n')


def update_cache():
    global cashe_perm

    with open("Diary.txt", "r", encoding="utf-8") as file1:
        cashe_perm = []

        for line in file1:
            cashe_perm.append(line.strip())


def show_cashe():
    for i in cashe_perm:
        print(i)


if __name__ == "__main__":
    while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Выйти")

        choice = input("Выбери действие: ")

        match choice:
            case "1":
                note = input("Какую запись вы хотите добавить: ")
                add_note(note)
                cache_is_valid = False

            case "2":
                if not cache_is_valid:
                    update_cache()
                    cache_is_valid = True

                show_cashe()

            case "3":
                break

            case _:
                print("Такого пункта нет")
        