import math
radius = int(input("Введите радиус круга: "))
if radius>=0 :
    print("Площадь = ", round( math.pi * radius ** 2, 2))
else :
    print("Введено не положительное число")
