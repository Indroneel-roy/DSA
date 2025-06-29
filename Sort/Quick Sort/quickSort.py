def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]       # Elements less than pivot
    middle = [x for x in arr if x == pivot]    # Elements equal to pivot
    right = [x for x in arr if x > pivot]      # Elements greater than pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [10, 5, 2, 3, 7, 6, 1, 8, 4, 9]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
