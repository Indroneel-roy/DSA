#find left and right child and parent node
def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def parent(i):
    return i // 2

def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)
    
    if l <= heap_size and heap[i] < heap[l]:
        largest = l
    else: 
        largest = i
    if r <= heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)    
        
def extract_max(heap, heap_size):
    if heap_size < 1:
        return None, heap_size
    max_item = heap[1]
    heap[1] = heap[heap_size]
    heap_size -= 1
    max_heapify(heap, heap_size, 1)
    return max_item, heap_size

def insert_key(heap, heap_size, node):
    heap_size += 1
    # Extend the heap list if necessary
    if heap_size >= len(heap):
        heap.append(node)
    else:
        heap[heap_size] = node
    i = heap_size
    
    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)
    return heap_size

def increase_key(heap, i, new_key):
    if new_key < heap[i]:
        print("Error: New key is smaller than current key")
        return
    
    heap[i] = new_key
    
    # Bubble up to maintain max heap property
    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)

def decrease_key(heap, heap_size, i, new_key):
    if new_key > heap[i]:
        print("Error: New key is larger than current key")
        return
    
    heap[i] = new_key
    # Bubble down to maintain max heap property
    max_heapify(heap, heap_size, i)

def build_max_heap(arr):
    heap_size = len(arr) - 1  # Excluding index 0
    # Start from the last non-leaf node and heapify
    for i in range(heap_size // 2, 0, -1):
        max_heapify(arr, heap_size, i)
    return heap_size

def print_heap(heap, heap_size):
    print("Heap:", [heap[i] for i in range(1, heap_size + 1)])

def heap_sort(arr):
    # Build max heap
    heap_size = build_max_heap(arr)
    
    # Extract elements one by one
    for i in range(len(arr) - 1, 1, -1):
        # Move current root to end
        arr[1], arr[i] = arr[i], arr[1]
        heap_size -= 1
        # Heapify the reduced heap
        max_heapify(arr, heap_size, 1)

# Example usage and testing
if __name__ == "__main__":
    # Initialize heap (index 0 is unused for easier calculation)
    heap = [0, 16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    heap_size = len(heap) - 1
    
    print("Original heap:")
    print_heap(heap, heap_size)
    
    # Test increase_key
    print("\nIncreasing key at index 9 from 1 to 15:")
    increase_key(heap, 9, 15)
    print_heap(heap, heap_size)
    
    # Test insert_key
    print("\nInserting key 20:")
    heap_size = insert_key(heap, heap_size, 20)
    print_heap(heap, heap_size)
    
    # Test extract_max
    print("\nExtracting maximum:")
    max_val, heap_size = extract_max(heap, heap_size)
    print(f"Extracted: {max_val}")
    print_heap(heap, heap_size)
    
    # Test decrease_key
    print("\nDecreasing key at index 2 from 15 to 5:")
    decrease_key(heap, heap_size, 2, 5)
    print_heap(heap, heap_size)
    
    # Test heap sort
    print("\nTesting heap sort:")
    arr_to_sort = [0, 4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Before sorting:", arr_to_sort[1:])
    heap_sort(arr_to_sort)
    print("After sorting:", arr_to_sort[1:])