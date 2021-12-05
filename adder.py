def adder(*nums):
    return sum(nums)    



numbers_input = input("Введите числа,сумму которых хотите найти: ")
try:
    numbers = [float(number) for number in numbers_input.split()]
    print("Сумма =" ,adder(*numbers))
except ValueError:
    print("Некорректный ввод")







    



        




