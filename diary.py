cashe_perm = []
cashe_temp = []


def add_note(tekst):
    with open ("Diary.txt", "a", encoding = "utf-8") as file1:
        file1.write(tekst + "\n")
            

def add_all():
    cashe_temp.clear()
    with open ("Diary.txt", "r", encoding = "utf-8") as file1:
        lines = file1.readlines()
        for line in lines:
            cashe_temp.append(line.strip())

def update_cache_if_needed():
    global cashe_perm
    add_all()
    if cashe_perm != cashe_temp:
        cashe_perm = cashe_temp.copy()


def show_cashe():
    for i in cashe_perm:
        print(i)
       
        

if __name__ == "__main__":
   while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Выйти")

        choice = input ("Выбери действие :")

        match choice:
            case "1":
                note = input("Какую запись вы хотите добавить: ")
                add_note(note)
            case "2":
                update_cache_if_needed()
                show_cashe()
            case "3":
                break

        

          
