import time

def selection_sort_with_steps(arr):
    time_start = time.time()
    steps = []
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        if min_idx != i:
            steps.append({"i": i, "j": min_idx})
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    time_end = time.time()
    return arr, steps, time_end - time_start
