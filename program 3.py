x = float(input("Введи 1-ое число: "))
y = float(input("Введи 2-ое число: "))
z1 = x+y
print ("Сумма: ", round(z1, 2))
z2 = x-y
print ("Разность: ", round (z2, 2))
z3 = x*y
print ("Произведение: ", round (z3, 2))
if y!=0 :
    z4 = x/y
    z6 = x//y
    print ("Деление: ", round (z4, 2))
    print ("Деление по модулю", round(abs(z4), 2))
    print ("Целочисленное деление", round(z6, 2))
else : print ("Деление на 0 невозможно")
z5 = x**y
print ("Возведение в степень: ", round(z5, 2))

