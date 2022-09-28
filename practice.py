# Напишите программу, которая выводит все числа от 1 до 100, кроме чисел 7, 17, 29 и 78.
# for i in range(1, 101)
for i in range(1, 101):
if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
# #     print(i)
# for i in range(1, 101):
# # if i == 17:
# #         break
# #     print(i)
# а не нужно добавить
# i += 1 ?
# my_list = [1, 2, 3, 4, 5, 6]
# new_list = list(map(lambda x: x*2, my_list))

# def func(x):
#     return x * 2

# current_list = [5, 15, 20, 30, 50, 55, 75, 60, 70]
# summa = reduce((lambda x, y: x + y), current_list)

# tables = [lambda x = x: x*10 for x in range(1, 11)]
# for table in tables:
#     print(table())

# a = (lambda x, y, z: x + y + z)(1, 2, 3);
# print(a)
# b = (lambda x, y, z=3: x + y + z)(1, 2);
# print(b)
# c = (lambda x, y, z=3: x + y + z)(1, y=2);
# print(c)
# d = (lambda *args: sum(args))(1,2,3);
# print(d)
# e = (lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3);
# print(e)
# f = (lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3);
# print(f)
#
