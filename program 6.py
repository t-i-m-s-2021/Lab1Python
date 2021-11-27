place = [0,0]
where = input("Старт из точки (0;0). Куда вы хотите пойти: направо/налево/вверх/вниз? ")
if (where == "направо"):
    place[0] +=1
elif (where == "налево"):
    place[0]  -=1
elif (where == "вверх"):
    place[1] +=1
elif (where == "вниз"):
    place[1] -=1
else:
     print("Некорректный ввод")
     exit

print(f"Текущее положение персонажа: {place} ")

