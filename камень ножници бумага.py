import random

score_b = 0  # b = player
score_a = 0  # a = computer
while True:
    b = str(input("что ставите?(камень, ножницы, бумага): "))
    a = random.choice(["камень", "бумага", "ножницы"])
    print("программа поставила", a)
    if a == b:
        print("ничья")
    elif a == "камень" and b == "ножницы":
        print("вы проиграли")
        score_a += 1
    elif a == "камень" and b == "бумага":
        print("вы выйграли!")
        score_b += 1
    elif a == "ножницы" and b == "камень":
        print("вы выйграли!")
        score_b += 1
    elif a == "ножницы" and b == "бумага":
        print("вы проиграли")
        score_a += 1
    elif a == "бумага" and b == "камень":
        print("вы проиграли")
        score_a += 1
    elif a == "бумага" and b == "ножницы":
        print("вы выйграли!")
        score_b += 1
    else:
        print("выберите что-либо из предоставленого списка")
    print(f"ваш уровень: {score_b}")
    print(f"уровень компьютера {score_a}")
    n = input("хотите сыграть еще раз?: ")
    if n == "нет":
        print("До новых встречь!")
        exit()
