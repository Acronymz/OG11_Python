def myFunc ():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    if a < b:
        print("Плохой негативный текст!")
    elif a > b:
        print("Хороший позитивный текст!")
    else:
        print("Баланс в природе не нарушен!");

myFunc()