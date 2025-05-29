
import time
def bubble_sort_with_steps(arr):
    time_start = time.time()
    steps = []
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                steps.append({"i": j, "j": j + 1})
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    time_end = time.time()
    return arr, steps, time_end - time_start
