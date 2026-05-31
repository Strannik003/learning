
import csv

count_of_students = 0

def add_student():
    name = input ("как ховут студента ")
    age = int(input("Возраст: "))
    mark = int(input("Какой средний балл? "))
    with open("students_base.csv","a", encoding="utf-8", newline="") as file:
        writer=csv.writer (file)
        writer.writerow([name,age,mark])

def read_students():
    with open("students_base.csv","r", encoding="utf-8", newline="") as file:
        lines=csv.reader (file)
        for line in lines:
            print(line)

def analize():
    global count_of_students
    with open("students_base.csv","r", encoding="utf-8", newline="") as file:
        lines=csv.reader (file)
        next(lines)
        for line in lines:
            if int(line[2])>=4:
                print(line)
                count_of_students +=1
        if count_of_students == 0:
            print("Отличников нет")


if __name__ == "__main__":
    try:
        with open("students_base.csv","r", encoding="utf-8") as file:
            writer=csv.reader (file)
    except FileNotFoundError:
        print("no file")

    with open("students_base.csv", "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Возраст", "Средний балл"])


    while True:
            print("\nМеню:")
            print("1. Добавить студента")
            print("2. Показать всех студентов")
            print("3. Показать студентов с оценками выше 4")
            print("4. Выйти")

            choice = input ("Выбери действие :")
            match choice:
                case "1":
                    add_student()
                case "2":
                    read_students()
                case "3":
                    analize()
                case "4":
                    break

