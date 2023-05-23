# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
# 5
# 1 2 4

# 17
# 1 2 4 8 16

n = input("Пожалуйста, введите Ваше число: ")
try:
    n = int(n)
    if n <= 0:
        print("Нет ни одной степени двойки в заданном диапазоне")
    else:
        degree = 0
        while 2**degree < n:
            print(f"{2**degree}", end=" ")
            degree = degree + 1
except ValueError:
    print("Пожалуйста, введите Ваше число в числовом формате")