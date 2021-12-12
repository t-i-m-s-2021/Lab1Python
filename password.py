min_length = 6
""" в результате успешного выполнения работы функция вернет True
"""

def Password_verification(password):
    if (len(password)< min_length):
        return False
    elif (str(password).isalpha()):
        return False
    elif (str(password).isnumeric()):
        return False
    elif (str(password).lower().__contains__('password')):
        return False
    else:
        return True

password = input("Введите ваш пароль: ")
if(Password_verification(password)):
    print("Ваш пароль принят!")
else:
    print("Введенный пароль не соответсвует требованиям!")
