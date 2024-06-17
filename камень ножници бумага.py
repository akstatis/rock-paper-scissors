import random

def question():
    n = input("хотите сыграть еще раз?: ")
    if n == "да":
        code()
    else:
        print("До новых встречь!")
        exit()

def code():
    b = str(input("что ставите?(камень, ножницы, бумага): "))
    a = random.choice(["камень", "бумага", "ножницы"])
    print("программа поставила", a)
    if a == b:
        print("ничья")
    elif a == "камень" and b == "ножницы":
        print("вы проиграли")
    elif a == "камень" and b == "бумага":
        print("вы выйграли!")
    elif a == "ножницы" and b == "камень":
        print("вы выйграли!")
    elif a == "ножницы" and b == "бумага":
        print("вы проиграли")
    elif a == "бумага" and b == "камень":
        print("вы проиграли")
    elif a == "бумага" and b == "ножницы":
        print("вы выйграли!")
    else:
        print("выберите что-либо из предоставленого списка")
        code()
    question()




code()
