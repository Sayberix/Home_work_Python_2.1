# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = input("введите номер четверти: ")

if quarter.isdigit() == True:
    match quarter.split():
        case ["1"]: print('в 1-ой четверти диапазон координат должен быть: x > 0 и y > 0:')
        case ["2"]: print('во 2-ой четверти диапазон координат должен быть: x < 0 и y > 0:')
        case ["3"]: print('в 3-ей четверти диапазон координат должен быть: x < 0 и y < 0:')
        case ["4"]: print('в 4-ой четверти диапазон координат должен быть: x > 0 и y < 0:')
        case _: print('неверно введенная четверть! Четверть должна быть от 1 до 4! Программа завершает работу!')
else:
    print('неверный ввод! Введеный символ должны быть числом!')