from random import randint
set1 =set(randint(-100,100) for i in range (0,10))
set2 =set(randint(-100,100) for i in range (0,10))
print("Первый набор: ", set1)
print("Второй набор: ", set2)

set3 = set1 & set2
set4 = set1-set2
set5 = set2-set1
set6 = ((set2-set1)|(set1-set2))
if (len(set3) == 0):
    print("В наборах нет одинаковых эл-ов")
else:
    print(f"Элементы, входящие в оба набора одновременно: {set3} ")
if (len(set4) == 0):
    print(f"Наборы совпали")
else:
    print(f"Элементы, входящие только в 1-ый набор: {set4}")
    print(f"Элементы, входящие только во 2-ой набор: {set5}")
    print(f"Элементы, содержащиеся или только 1, или только во 2 наборе: {set6}")

