# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint
numbers = []
for i in range(24):
    numbers.append(randint(2, 9))

new_list = []
for elem in set(numbers):
    if numbers.count(elem) > 1:
        new_list.append(elem)


print(f'{numbers}')
print(f'{new_list}')