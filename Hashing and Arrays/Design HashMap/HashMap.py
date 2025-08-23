# Problem Link : https://leetcode.com/problems/design-hashmap/description/
from typing import List
class MapNode:
    def __init__(self, key = None, val = None, next = None):
        self.key= key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.hashMap = [MapNode() for _ in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        curr = self.hashMap[key % len(self.hashMap)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = MapNode(key, value)
        
    def get(self, key: int) -> int:
        curr = self.hashMap[key % len(self.hashMap)]
        while curr.next:
            if curr.next.key == key:
                return curr.next.val
            curr = curr.next
        return -1    
      
    def remove(self, key: int) -> None:
        curr = self.hashMap[key % len(self.hashMap)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
# Example usage
if __name__ == "__main__":
    hashMap = MyHashMap()
    hashMap.put(2, 3)
    print(hashMap.get(2))   # 3
    hashMap.put(2, 5)       # update key 2
    print(hashMap.get(2))   # 5
    print(hashMap.get(10))  # -1 (not found)
    hashMap.remove(2)
    print(hashMap.get(2))   # -1 (removed)
