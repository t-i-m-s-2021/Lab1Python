import math
print(" Введите коэффициенты для уравнения ax^2+bx+c=0:")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if (a == 0):
    print("Ваше уравнение не является квадратным!")
else:
    D = b**2-4*a*c
    print(f"Дискриминант = {D}")
    if D>0:
        x1 = (-b + math.sqrt(D))/(2*a)
        x2 = (-b - math.sqrt(D))/(2*a)
        print(f"Корни уравнения: {x1} и {x2}")
    elif (D==0):
        x= -b/(2*a)
        print(f"Корень уравнения: {x}")
    else:
        print("Введенное уравнение не имеет корней")
    


