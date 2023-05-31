# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint


def init_list(number):
    my_list = [randint(0, 99) for i in range(number)]
    return my_list


n = input("Введите количество кустов: ")
if n.isdigit() and int(n) > 0:
    n = int(n)
    row = init_list(n)
    print("Ваш список:")
    print(row, sep=", ")
    if n <= 3:
        max = sum(row)
        max_index = 0
    else:
        left_index = -1
        index = 0
        right_index = -len(row) + 1
        max = 0
        max_index = 0
        while index < len(row):
            sum = row[left_index] + row[right_index] + row[index]
            if max < sum:
                max = sum
                max_index = index
            left_index += 1
            right_index += 1
            index += 1
    print(
        f"Максимальное количество возможное для сбора равное {max} можно получить у куста № {max_index+1}"
    )
else:
    print("Введите количество кустов в виде натурального числа!")