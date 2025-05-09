# Problem Link : https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Calculate the length of the linked list
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        #Specital case if need to remove head of the link list
        if n == length:
            return head.next
        
        #reach berfore the target index from end of the list
        current = head
        for _ in range(length - n - 1):
            current = current.next 
        
        if current and current.next:
            current.next = current.next.next 
        
        return head                    

def list_to_linkedlist(items):
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = 2  # remove 2nd node from the end -> remove '4'
    head = list_to_linkedlist(arr)
    sol = Solution()
    updated = sol.removeNthFromEnd(head, n)
    print(linkedlist_to_list(updated))  # Output: [1, 2, 3, 5]
    