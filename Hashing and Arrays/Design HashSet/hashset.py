# Problem Link : https://leetcode.com/problems/design-hashset/description/
from typing import List
class HashNode:
    def __init__(self, val):
        self.val = val
        self.next = None
         

class MyHashSet:

    def __init__(self):
        self.hashSet = [HashNode(0) for i in range(10**4)]
     
        

    def add(self, key: int) -> None:
        curr = self.hashSet[key % len(self.hashSet)]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = HashNode(key)    
       

    def remove(self, key: int) -> None:
        curr = self.hashSet[key % len(self.hashSet)]
        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
                return
            curr = curr.next
       
        
    def contains(self, key: int) -> bool:
        curr = self.hashSet[key % len(self.hashSet)]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False
if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)      
    myHashSet.add(2)      
    print(myHashSet.contains(1))  # True
    print(myHashSet.contains(3))  # False
    myHashSet.add(2)      
    print(myHashSet.contains(2))  # True
    myHashSet.remove(2)   
    print(myHashSet.contains(2))  # False
            
        