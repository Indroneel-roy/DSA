#Problem Link : https://leetcode.com/problems/reverse-linked-list/description/
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev #Reversing the direction of linked list
            prev = curr
            curr = nxt
        return prev    
def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = list_to_linkedlist(arr)
    sol = Solution()
    res = sol.reverseList(head)

    # Print the reversed list
    while res:
        print(res.val, end=" -> " if res.next else "\n")
        res = res.next