import random

def twoLists():
    set1 = random.sample(range(20), 10)
    print("Первый список: " + str(set1))
    set2 = random.sample(range(20), 10)
    print("Второй список: " + str(set2))
    result = set(set1).union(set(set2))
    print("Общий список: " + str(result))

twoLists()
