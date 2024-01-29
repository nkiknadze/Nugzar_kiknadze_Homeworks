

import random
import time

# #Task_N1
# '''
# 1.	დაალაგე შემთხვევით დაგენერირებული 10 ელემენტიანი სია sort() მეთოდის გამოყენებით (ზრდადობით).
# '''

# print("Task_N1")

# a = [random.randint(1, 100) for i in range(10)]

# print(f"Unsorted List: ", a)

# a.sort()
# print(f"Sorted List (Asc):", a)
# print()

#task_N2
# print("task_N2")

# a = [random.randint(1, 100) for i in range(10)]

# print(f"Unsorted List:", a)
# b = sorted(a, reverse=True)
# print(f"Sorted List (Desc): ", b)
# print()

#Task_N3
print("task_N3")


def bubble(arr):
    n = len(arr)

    for i in range(n):
        for b in range(0, n-i-1):
            if arr[b] > arr[b+1]:
                arr[b], arr[b+1] = arr[b+1], arr[b]

def selection(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for b in range(i+1, n):
            if arr[b] < arr[min_index]:
                min_index = b

        arr[i], arr[min_index] = arr[min_index], arr[i]

def time_and_sort(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Generate lists of random integers
small = [random.randint(1, 1000) for _ in range(1000)]
medium = [random.randint(1, 2000) for _ in range(2000)]
long = [random.randint(1, 3000) for _ in range(3000)]

s = len(small)
m = len(medium)
l = len(long)
print(f"small  len: {s}" )
print(f"medium len: {m}" )
print(f"long   len: {l}" )
print("---")

# Measure time for Bubble Sort
bubble_sort_time_small = time_and_sort(bubble, small.copy())
bubble_sort_time_medium = time_and_sort(bubble, medium.copy())
bubble_sort_time_long = time_and_sort(bubble, long.copy())

# Measure time for Selection Sort
selection_sort_time_small = time_and_sort(selection, small.copy())
selection_sort_time_medium = time_and_sort(selection, medium.copy())
selection_sort_time_long = time_and_sort(selection, long.copy())

# Display results
print("Bubble Sort Time (Small):", bubble_sort_time_small)
print("Bubble Sort Time (Medium):", bubble_sort_time_medium)
print("Bubble Sort Time (Long):", bubble_sort_time_long)
print("---")
print("Selection Sort Time (Small):", selection_sort_time_small)
print("Selection Sort Time (Medium):", selection_sort_time_medium)
print("Selection Sort Time (Long):", selection_sort_time_long)
print("---")
print("Time Difference (Bubble Sort - Selection Sort) for Small:", bubble_sort_time_small - selection_sort_time_small)
print("Time Difference (Bubble Sort - Selection Sort) for Medium:", bubble_sort_time_medium - selection_sort_time_medium)
print("Time Difference (Bubble Sort - Selection Sort) for Long:", bubble_sort_time_long - selection_sort_time_long)
