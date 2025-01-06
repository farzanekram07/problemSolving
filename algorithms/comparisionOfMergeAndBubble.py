import time

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Test and Compare
def compare_sorts():
    test_case = [64, 34, 25, 12, 22, 11, 90]  
    print("Original List:", test_case)

    # Bubble Sort
    arr_bubble = test_case.copy()
    start_time = time.time()
    bubble_sort(arr_bubble)
    bubble_time = time.time() - start_time
    print("Bubble Sorted:", arr_bubble)
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")

    # Merge Sort
    arr_merge = test_case.copy()
    start_time = time.time()
    merge_sort(arr_merge)
    merge_time = time.time() - start_time
    print("Merge Sorted:", arr_merge)
    print(f"Merge Sort Time: {merge_time:.6f} seconds")

compare_sorts()
