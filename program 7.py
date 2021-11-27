place = [0,0]
print("Старт из точки (0;0). Куда вы хотите пойти: направо/налево/вверх/вниз? ")
while True:
    where = input()
    early =[place[0], place[1]] 
    if (where == "направо"): 
        place[0] +=1
    elif (where == "налево"):
        place[0]  -=1
    elif (where == "вверх"):
        place[1] +=1
    elif (where == "вниз"):
        place[1] -=1
    else:
        if (where == "Конец"):
            print(f"Игра закончена, текущее положение персонажа: {place} ")
        else:
             print("Некорректный ввод")
        break
    print(f"Осуществлен переход от {early} к {place}")
    print("Для продолжения вводи направо/налево/вверх/вниз: ")
    print("Для завершения игры, введи слово Конец: ")    
    
