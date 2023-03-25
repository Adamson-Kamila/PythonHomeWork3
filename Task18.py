# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

n = int(input('Введите длину n: '))
arr = [random.randint(1, 50) for i in range(n)]
# arr = [i for i in range(1, n, 4)]
print(arr)
arr.sort()
print(arr)
x = int(input('Введите натуральное число x: '))

# print(arr[1:-1])

if x <= arr[0]:
    print(arr[0])
elif x >= arr[-1]:
    print(arr[-1])
else:
    for i in range(1, len(arr)): # 1 - с элемента под индексом №1, [1:] - до конца массива, не включая
        # последний элемент.
        if x == arr[i]:
            print(arr[i])
            break
        elif arr[i] > x:
            if arr[i] - x > x - arr[i-1]:
                print(arr[i-1])
                break
            elif arr[i] - x == x - arr[i-1]:
                print(arr[i], arr[i-1])
                break
            else:
                print(arr[i])
                break

