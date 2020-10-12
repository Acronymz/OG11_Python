import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
randomNumbers = random.sample(numbers, 5)
print(randomNumbers)
userNum = int(input("Введите одну из перечисленных выше цифр: "))
if userNum in randomNumbers:
    n = randomNumbers.index(userNum) + 1
    result = "Данная цифра находится под индексом " + str(n)
    print(result)
else:
    print("Такой цифры нет в списке")