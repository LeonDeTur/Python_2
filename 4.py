# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции вводятся с клавиатуры.

num = -int(input())
list = []
for _ in range ((-num)*2+1):
    list.append(num)
    num = num + 1

print(f"Список: {list}")
print(f"Введите позиции указанных элементов построчно (от 0 до {num}, где 0 - индекс первого чисда в списке.) ")
first_position = int(input())
second_position = int(input())
print(f"Произведение указанных элементов равно {list[first_position]*list[second_position]}.")