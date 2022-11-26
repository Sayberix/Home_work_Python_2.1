# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

axInp = input("введите координаты точки x отрезка a: ")
ayInp = input("введите координаты точки y отрезка a: ")
bxInp = input("введите координаты точки x отрезка b: ")
byInp = input("введите координаты точки y отрезка b: ")

if (axInp.isdigit() and ayInp.isdigit() and bxInp.isdigit() and byInp.isdigit()):
    ax = int(axInp)
    ay = int(ayInp)
    bx = int(bxInp)
    by = int(byInp)
    if ((ax != 0 and ay != 0) and (bx != 0 and by != 0)):
        import math as np
        distance = float(np.sqrt(abs((bx - ax)**2) + ((by - ay)**2)))
        print(f'расстояние между точками равно: {round(distance,3)}')
    else:
        print('неверный ввод! Введеные координаты не должны быть равны нулю!')
else:
    print('неверный ввод! Введеные координаты должны быть числом!')