def countSort(arr):
    if not arr:
        return []
    max_val = max(arr)
    
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    
    sorted_list = []
    for i in range(len(count)):
        sorted_list.extend([i] * count[i])
    
    return sorted_list
# Example usage:
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = countSort(arr)
print("Sorted array:", sorted_arr)