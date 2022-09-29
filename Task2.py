# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# ¬ - инвесия: Логическое "не"
# V - дизъюнкция: Логическое "или", Высказывание ложно, если все значения ложны
# ⋀ - конъюнкция: Логическое "и", Высказывание истинно, когда все значения истинны
# not (X or Y or Z) = not X and not Y and not Z

import random
bool_list = [True, False]
x = random.choice(bool_list)
y = random.choice(bool_list)
z = random.choice(bool_list)
print(f'{x} {y} {z}')
a = not (x or y or z)
b = not x and not y and not z
print(a == b)

# не хватает знаний по синтаксису для пользовательского ввода, циклов на неправильный ввод
# буду рад комментариям
