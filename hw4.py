# Задание 4.1
# Напишите функцию square, принимающую 1 аргумент — сторону квадрата,
# и возвращающую 3 значения(с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
#import math

# def get_square(side):
#   perimeter = side * 4
#   area = side**2
#   diagonal = math.sqrt(2) * side
#   return tuple([perimeter, area, diagonal])
# print(get_square(10))
# ____________________________
import math as m
def get_square(side):
    return(side * 4, side ** 2, round((m.sqrt(2) * side), 2))
square_data = get_square(int(input('Enter square side: ')))
print(f'square area:{square_data[0]}, {square_data[0]}, {square_data[0]}')
print(get_square(10))

# Задание 4.2
# Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и
# выводит их построчно в формате аргумент: значение.
# Например: name: John last_name: Smith age: 35 position: web developer

def coworker(**kwargs):
  for key, value in kwargs.items():
      print(f'{key}: {value}')

  coworker(name='John', last_name='Smith', age=35, position='web developer')
# _______________________
#   print('{}: {}'.format(key,value))

# Задание 4.3
# Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список,
# содержащий только положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# filtered_list = [x for x in my_list if x >= 0]
# print(filtered_list)
#__________________________________________________
# filtered_list =list(filter(lambda x: (x >= 0), my_list))
# print(filtered_list)

# Задание 4.4 Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# print(reduce(lambda x, y: x*y, filtered_list))

# Задание 4.5 Создайте файл my_calc.py и пропишите в нем минимум 4 функции,
# выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.

# from my_calc import *
# print(sum_1(10,9))
# print(sub_2(10,20))
# print(mult_3(5,6))
# print(div_4(10,0))
# print(div_4(10,5))

