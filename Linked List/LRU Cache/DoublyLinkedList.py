# Problem Link : https://leetcode.com/problems/lru-cache/description/
from typing import List
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]   

def test_lru_cache():
    print("Running tests...")

    # Create a cache with capacity 2
    lru = LRUCache(2)
    
    # Test insertion
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1  # returns 1

    # Since 1 was accessed recently, 2 is now LRU
    lru.put(3, 3)           # evicts key 2
    assert lru.get(2) == -1 # returns -1 (not found)

    assert lru.get(3) == 3  # returns 3

    # Now 1 is LRU
    lru.put(4, 4)           # evicts key 1
    assert lru.get(1) == -1 # returns -1 (not found)
    assert lru.get(3) == 3  # returns 3
    assert lru.get(4) == 4  # returns 4

    # Update value and check recency
    lru.put(4, 40)
    assert lru.get(4) == 40

    print("All tests passed.")

test_lru_cache()
            