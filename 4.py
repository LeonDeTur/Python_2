# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры.
import random

num = -int(input())
list = []
for _ in range ((-num)*2+1):
    list.append(random.randint(num, -num))
index_list = []

print(f"Список: {list}")
print(f"Введите позиции указанных элементов построчно (от 0 до {num}, где 0 - индекс первого чисда в списке.) ")

enter = int(input("Введите позицию элемента. Если вы закончили, введит не число: "))
while enter is int:
    enter = int(input("Введите позицию элемента. Если вы закончили, введит не число: "))
    index_list.append(enter+1)

multiple_list = []
for _ in index_list:
    tmp = index_list[_]
    multiple_list.append(list[tmp])

def multiple_entered_positions (*args_1,):
    result = 1
    for _ in len(args_1):
        result = result * args_1[_]
    return result

print(f"Произведение элементов введённых позиций: {multiple_entered_positions(*multiple_list)}")

