parol = input("Введите пароль: ")
counterupperr=0
counterlowerr=0
counternumbers=0
if len(parol) < 8:
    print("Пароль короткий КАК ТВОЙ ЧЛЕН, он должен быть не менее 8 символов")
else:
    for i in parol:
        print(i, end="")
        if i.isupper():
            counterupperr+=1
        else:
            counterupperr+=0
        if i.isdigit():
            counternumbers+=1
        else:
            counternumbers+=0
        if i.islower():
            counterlowerr+=1
        else:
            counterlowerr+=0
    if counterupperr == 0:
        print("Пароль должен содержать хотя бы одну заглавную букву")
    elif counternumbers == 0:
        print("Пароль должен содержать хотя бы одну цифру")
    elif counterlowerr == 0:
        print("Пароль должен содержать хотя бы одну строчную букву")
    else:
        print("Пароль хороший")