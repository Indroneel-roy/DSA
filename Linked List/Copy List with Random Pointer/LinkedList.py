#Problem Link : https://leetcode.com/problems/copy-list-with-random-pointer/description/
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToNew[curr]   
            copy.next = oldToNew[curr.next] #If I use curr.next that will point to the origin list
            copy.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]    