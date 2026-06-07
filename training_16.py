# Программа, которая создаёт 100 случайных чисел, сохраняет их в файл и считает среднее значение.
import random, statistics, json

if __name__=='__main__':
    list_of_numbers = []
    for i in range(1,101):
        x = random.randint(1,101)
        list_of_numbers.append(x)
    print(list_of_numbers)
    mean = statistics.mean(list_of_numbers)
    print(f'Средняя для этой выборки : {mean} ')

    with open("numbers.json","w", encoding="utf-8") as file:
        json.dump(list_of_numbers, file, indent=4)

    

    

