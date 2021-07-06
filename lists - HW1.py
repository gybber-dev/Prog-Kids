"""
Домашнее задание:

Внизу дан массив block_list с ID блоков майнкрафта.
Тебе нужно создать пустой массив my_blocks. Далее, заполни этот 
массив элементами из block_list, но только теми, чей id больше,
чем id бедрока.

Пример:
print(block_list) -> [5, 14, 9, 1, 20, 5, 6, 15, 7, 13]
print(my_blocks)  -> [14, 9, 20, 15, 13]

Далее, напиши код, который выведет все блоки листа my_blocks одной полоской в minecreaft.
"""

import mc
import random

block_list = []

for i in range(10):
    block_list.append(random.randint(1, 22))

print(block_list)

# допиши свой код ниже
