def fibonacci(n):
    if (n>0):
        if n in (1,2):
            return 1
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return ("Номер числа может быть только положительным!")


try:
    print(fibonacci(int(input("Введите номер числа Фибоначчи: "))))
except ValueError:
    print("Некорректный ввод!")
