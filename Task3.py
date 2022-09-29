# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def get_int_number_notZero(num):    # Не знаю насколько э
    while True:
        try:
            value = int(num)
            if value == 0:
                raise ValueError
        except ValueError:
            num = input('Введите натуральное число, не равное нулю: ')
        else:
            return value

x = get_int_number_notZero(input('Введите координату Х, кроме 0: '))
y = get_int_number_notZero(input('Введите координату Y, кроме 0: '))

if x > 0 and y > 0: print('Точка в 1 четверти плоскости')
elif x < 0 and y > 0: print('Точка во 2 четверти плоскости')
elif x < 0 and y < 0: print('Точка в 3 четверти плоскости')
elif x > 0 and y < 0: print('Точка в 4 четверти плоскости')