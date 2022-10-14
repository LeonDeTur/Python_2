# Реализуйте алгоритм перемешивания списка.

import random

list = [1,2,3,4,5,6,7]
print(f"Изначальный массив: {list}")

list_index = [len(list)]
randomed_list = [(len(list))]

list_index = random.sample(range(len(list)), len(list))
randomed_list_index = random.sample(range(len(list)), len(list))
count = 0

while count < len(list)-1:
    tmp_index = list_index[count]
    tmp = int(list[tmp_index])
    tmp_index = randomed_list_index[count]
    randomed_list.insert(tmp_index, tmp)
    count = count + 1

print(f"Перемешанынй массив: {randomed_list}")

