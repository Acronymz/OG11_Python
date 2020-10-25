number = int(input("Введите число:"))
def watsons(a):
    a = [int(x) for x in str(number)]
    result = sum(a)
    print("Сумма елементов: " + str(result))
watsons(number)