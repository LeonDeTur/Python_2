# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11


num = input()
result = 0
for i in range (len(num)):
    if num[i].isdigit():
        result = result + int(num[i])
print(result)