# Array = [19, 7, 17, 3, 5, 12, 10, 1, 2] this maxheap left child of root will stay in 2*n nth possition and right child 2*n + 1 and index will start from 1
heap = [None] * 10
heap[1] = 19
heap[1*2] = 7
heap[1*2+1] = 17
heap[2*2] = 3
heap[2*2+1] = 5
heap[3*2] = 12
heap[3*2+1] = 10
heap[4*2] = 1
heap[4*2+1] = 2
print(heap)

#find left and right child and parent node
def left(i):
    return 2 * i
def right(i):
    return 2 * i + 1
def parent(i):
    return i // 2
print(heap[left(3)])

#Justyfy MaxHeap or not

def is_max_heap(H):
    n = len(H) - 1
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
    return True
if __name__ == "__main__":
    H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2] 
    print(H, is_max_heap(H))
    
        

