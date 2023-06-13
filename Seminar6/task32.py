# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону (т.е. не меньше заданного 
# минимума и не больше заданного максимума)

from random import randint

def init_list(number):
    my_list = [randint(0, 99) for i in range(number)]
    return my_list

minimum = int(input("Введите минимальный порог поиска: "))
maximum = int(input("Введите максимальный порог поиска: "))
my_list = init_list(randint(0, 31))
print(my_list)
result = []
for i in range(len(my_list)):
    if (my_list[i]>minimum and my_list[i]<maximum):
        result.append(i)
print(result)