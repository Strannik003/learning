import os 
if os.path.exists("Diary.txt"):

    def add_note():
        tekst = input("Какую запись вы хотите добавить: ")
        with open ("Diary.txt", "a", encoding = "utf-8") as file1:
            file1.write(tekst + "\n")
            

    def read_all():
        with open ("Diary.txt", "r", encoding = "utf-8") as file1:
           lines = file1.readlines()
           for line in lines:
               print(line.strip())
        
    
    while True:
        print("\nМеню:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Выйти")

        choice = input ("Выбери действие :")
        if choice == "1":
            add_note()
        if choice == "2":
            read_all()
        if choice == "3":
            break

        
            
else:
    print ("No file")
    