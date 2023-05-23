# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N)
# 0! = 1 Решить задачу используя цикл while

# my_number = int(input("Please, enter your number: "))
# factorial = 1
# if (my_number > 0):
#     if my_number<=1:
#         print(factorial)
#     else:
#         while (my_number>1):
#             factorial*=my_number
#             my_number = my_number - 1
#         print(f"Факториал = {factorial}")
# else:
#     print("Введите неотрицательное число!!")


# Дано натуральное число A > 1. Определите, каким по счету числом
# Фибоначчи оно является, то есть выведите такое число n,
# что φ(n)=A. Если А не является числом Фибоначчи, выведите
# число -1.

# my_number = int(input("Пожалуйста, введите число: "))
# if my_number < 0:
#     print("Пожалуйста, введите число больше 0")
# else:
#     number1 = 0
#     number2 = 1
#     number_position = 3
#     find_number = False
#     if my_number == 0:
#         print(1)
#     elif my_number == 1:
#         print(2)
#     else:
#         while number1+number2 <= my_number and not find_number:
#             if (number1+number2 == my_number):
#                 find_number = True
#                 print (number_position)
#             else:
#                 temp = number1
#                 number1 = number2
#                 number2 = temp + number1
#                 number_position +=1
#         if find_number==False:
#             print(-1)


# Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя
# нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как
# же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой
# строчке каждое. Здесь каждое число – это масса
# соответствующего арбуза. Все числа натуральные и не
# превышают 30000.

from random import randint
# watermelone_count = int(input("Пожалуйста, введите число арбузов: "))
# min = 10
# max = 1
# for i in range(watermelone_count):
#     watermelone_weight = randint(1,10)
#     print(watermelone_weight)
#     if watermelone_weight>max:
#         max = watermelone_weight
#     if watermelone_weight<min:
#         min = watermelone_weight
# print(f"Мой арбуз - {max} кг, тещин арбуз - {min} кг")


# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те,
# в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура
# ежедневно превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

temperature = randint(-10, 10)
print(f"Стартовая тепература {temperature} градусов")
days_count = 31+30+28
max = 0
thaw_days_count = 0
for i in range(days_count):
    print(temperature,sep=" ")
    if temperature > 0:
        thaw_days_count +=1
    else:
        if thaw_days_count>max:
            max = thaw_days_count
        thaw_days_count = 0
    delta = randint(-3, 3)
    temperature = temperature+delta
if thaw_days_count>max:
    max = thaw_days_count
print(f"Максимальная оттепель {max} дней")
