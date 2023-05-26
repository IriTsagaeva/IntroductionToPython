# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. Последняя строка содержит число X

from random import randint
list_size = int(input("Введите количество элементов массива: "))
if (list_size<=0):
    print("Пожалуйста, введите натуральное число!!!")
else:
    my_list = [randint(1,10) for i in range(list_size)]
    print(my_list)
    desired_element = int(input("Введите искомый элемент: "))
    count = 0
    for i in range(list_size):
        if my_list[i]==desired_element:
            count+=1

    print("Элемент {} встречается в списке {} раз".format(desired_element,count))