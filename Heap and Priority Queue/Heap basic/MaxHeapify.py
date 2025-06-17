#find left and right child and parent node
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1
def parent(i):
    return i // 2
# print(heap[left(3)])

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

##build max heap here we will start from a node which at least have one child means i from n/2 to 0
def build_max_heap(heap):
    heap_size = len(heap) - 1
    for i in range(heap_size // 2, 0, -1):
        max_heapify(heap, heap_size, i)

if __name__ == "__main__":
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print("Before heapify :", heap)
    build_max_heap(heap)
    print("After heapify :", heap)                      