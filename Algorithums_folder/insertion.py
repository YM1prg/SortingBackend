def insertion_sort_with_steps(arr):
    steps = []
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        insert_position = i
        while j >= 0 and arr[j] > key:
            insert_position = j
            j -= 1
        
        if insert_position != i:
            steps.append({"from": i, "to": insert_position})
            
            for k in range(i, insert_position, -1):
                arr[k] = arr[k - 1]
            
            arr[insert_position] = key
    
    return arr, steps