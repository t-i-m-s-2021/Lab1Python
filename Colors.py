colors = {'Синий':tuple([0,0,255]),'Зеленый':tuple([0,255,0]),'Красный':tuple([255,0,0]) }
print("Исходный словарь: ")
colors2=colors.copy()
y3 = input("Хотите просмотреть весь словарь цветов с кодировками? Если да, то нажмите +, если нет, то -: ")
if (y3 == '+'):
    for key, value in colors2.items():
        print(key,value)
else:
    exit
y2 = input("Хотите узнать RGB кодировку цвета? Если да, то нажмите +, если нет, то -: ")
if (y2 == "+"):
    color = input("Введите название цвета,для которого хотите узанть RGB код Синий/Зеленый/Красный: ")
    if (color == 'Синий'):
      print(colors2.get('Синий'))
    elif (color == 'Зеленый'): 
     print(colors2.get('Зеленый'))
    elif (color == 'Красный'):
     print(colors2.get('Красный'))
    else:
     print("Некорректный ввод")
     exit

else:
    exit
y = input("Хотите очистить исходный словарь? Если да, то нажмите +, если не, то -:")
if (y == "+"):
    colors2.clear()
    print("Словарь успешно очищен")
else:
    exit
if (len(colors2)!= 0):
    y1 = input("Хотите удалить цвет из словаря? Если да, то нажмите +, если не, то -:")
    if (y1 == "+"):
        try:
            delete_color = input("Введите название цвета, который хотите удалить: ")
            colors2.pop(delete_color)
            print("Измененный словарь:")
            for key, value in colors2.items():
                print(key,value)
        except KeyError:
            print("В словаре отсутствует такой цвет")
    else:
        exit
else:
    exit

    