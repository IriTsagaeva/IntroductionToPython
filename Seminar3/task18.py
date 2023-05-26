# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint
list_size = int(input("Введите количество элементов массива: "))
if (list_size<=0):
    print("Пожалуйста, введите натуральное число!!!")
else:
    my_list = [randint(1,10) for i in range(list_size)]
    print(my_list)
    desired_element = int(input("Введите искомый элемент: "))
    difference = float('+inf')
    for i in range(list_size):
        if my_list[i]-desired_element<difference:
            difference = my_list[i]-desired_element
            elements_value = my_list[i]
    print("Элемент списка, ближайший к значению {}, равен {}".format(desired_element,elements_value))