def comparison():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите шаг: "))
    while a <= b:
        print("Значение 'А' " + "Пока что нет")
        a = a + c
    print("Дождались! Финальный 'A' : " + str(a))


comparison()