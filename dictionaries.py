def firstDict(a, b):
    return{a: b}
a = input("Введите ключ для первого словаря:")
b = input("Введите значение для первого словаря:")
firstDictReady = firstDict(a, b)

def secondDict(c, d):
    return{c: d}
c = input("Введите ключ для второго словаря: ")
d = input("Введите значение для второго словаря: ")
secondDictReady = secondDict(c, d)

def merge_two_dicts(firstDictReady, secondDictReady):
    result = firstDictReady.copy()
    result.update(secondDictReady)
    return result

print(merge_two_dicts(firstDictReady, secondDictReady))


