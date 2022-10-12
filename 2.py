# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input())
count = 1
comp = 1
result = []
while count <= num:
    comp = comp * count
    result.append(comp)
    count = count + 1

print(result)
