# Problem Link : https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
import heapq
from typing import List

class KthLargest:
    # Constructor to initialize the object with k and nums list
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minHeap = nums
        
        # Convert the list into a min-heap
        heapq.heapify(self.minHeap)
        
        # Keep only the k largest elements in the heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    # Add a new value to the stream and return the k-th largest element
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        # If the heap exceeds size k, remove the smallest
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The root of the heap is the k-th largest element
        return self.minHeap[0]

# Only run this test when the script is executed directly
if __name__ == "__main__":
    # Initialize KthLargest with k = 3 and nums = [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    
    # Each add returns the current 3rd largest element
    print(kthLargest.add(3))   # Output: 4
    print(kthLargest.add(5))   # Output: 5
    print(kthLargest.add(10))  # Output: 5
    print(kthLargest.add(9))   # Output: 8
    print(kthLargest.add(4))   # Output: 8
