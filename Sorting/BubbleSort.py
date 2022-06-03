import random

arr = [random.randint(0, 10000) for x in range(0, 100)]

print(arr)

def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr) - 1):
            if arr[y] > arr[y + 1]:
                arr[y], arr[y + 1] = arr[y + 1], arr[y]
    return arr

print(bubble_sort(arr))