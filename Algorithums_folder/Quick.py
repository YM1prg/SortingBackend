def quick_sort_with_steps(arr):
    steps = []
    arr = arr.copy()
    
    def partition(low, high):
        pivot = arr[high]
        steps.append({"pivot": high})
        
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                if i != j: 
                    steps.append({"i": i, "j": j})
                    arr[i], arr[j] = arr[j], arr[i]
        
        
        if i + 1 != high:  
            steps.append({"i": i + 1, "j": high})
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
        
        return i + 1
    
    def quick_sort_helper(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_helper(low, pi - 1)
            quick_sort_helper(pi + 1, high)
    
    if len(arr) > 1:
        quick_sort_helper(0, len(arr) - 1)
    
    return arr, steps