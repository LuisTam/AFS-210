import time
import random

def quick_sort(a_list, start, end, pivot_selection):
    if start >= end:
        return

    if pivot_selection == "random":
        pivot = partition_random(a_list, start, end)
    elif pivot_selection == "median_of_three":
        pivot = partition_median_of_three(a_list, start, end)
    elif pivot_selection == "randomized_median_of_three":
        pivot = partition_randomized_median_of_three(a_list, start, end)
    else:
        pivot = partition_start(a_list, start, end)

    quick_sort(a_list, start, pivot - 1, pivot_selection)
    quick_sort(a_list, pivot + 1, end, pivot_selection)

def partition_start(a_list, start, end):
    return partition(a_list, start, end)

def partition_random(a_list, start, end):
    pivot_index = random.randint(start, end)
    a_list[start], a_list[pivot_index] = a_list[pivot_index], a_list[start]
    return partition(a_list, start, end)

def partition_median_of_three(a_list, start, end):
    mid = (start + end) // 2
    if a_list[start] > a_list[mid]:
        a_list[start], a_list[mid] = a_list[mid], a_list[start]
    if a_list[start] > a_list[end]:
        a_list[start], a_list[end] = a_list[end], a_list[start]
    if a_list[mid] > a_list[end]:
        a_list[mid], a_list[end] = a_list[end], a_list[mid]
    a_list[start], a_list[mid] = a_list[mid], a_list[start]
    return partition(a_list, start, end)

def partition_randomized_median_of_three(a_list, start, end):
    indices = [start, (start + end) // 2, end]
    random.shuffle(indices)
    a_list[start], a_list[indices[1]] = a_list[indices[1]], a_list[start]
    return partition(a_list, start, end)

def partition(a_list, start, end):
    pivot = a_list[start]
    low = start + 1
    high = end

    while True:
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        while low <= high and a_list[low] <= pivot:
            low = low + 1

        if low <= high:
            a_list[low], a_list[high] = a_list[high], a_list[low]
        else:
            break

    a_list[start], a_list[high] = a_list[high], a_list[start]
    return high

# Test and compare execution times
original_list = [x for x in range(1000)]
random.shuffle(original_list)

pivot_methods = ["start", "random", "median_of_three", "randomized_median_of_three"]

for pivot_method in pivot_methods:
    sorted_list = original_list.copy()
    start_time = time.time()
    quick_sort(sorted_list, 0, len(sorted_list) - 1, pivot_method)
    end_time = time.time()
    print(f"Pivot Method: {pivot_method}, Execution Time: {end_time - start_time:.6f} seconds")
