# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

# *Пример:*

#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

print(f"Введите целое натуральное число для нахождения результатов последовательности от одного, до введённого вами чсила.")
list = []
num = int(input())
i = 1
while i <= num:
    result = (1+1/i)**i
    list.append(round(result, 2))
    i = i + 1

print(f"{list}")
result = 0
for _ in range (len(list)):
    result = result + list[_]

print(f"Сумма:{result}")
