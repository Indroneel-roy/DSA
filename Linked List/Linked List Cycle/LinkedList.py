# Problem List : https://leetcode.com/problems/linked-list-cycle/description/
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # fast and slow pointers if there any cycle they must meet within n iteration
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False  
def list_to_linkedlist_with_cycle(items: List[int], pos: int) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    cycle_node = None

    if pos == 0:
        cycle_node = head

    for i, val in enumerate(items[1:], 1): # last 1 means index will also start from 1
        current.next = ListNode(val)
        current = current.next
        if i == pos:
            cycle_node = current

    # create cycle
    if cycle_node:
        current.next = cycle_node

    return head

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    pos = 1
    head = list_to_linkedlist_with_cycle(arr, pos)
    sol = Solution()
    res = sol.hasCycle(head)
    print(res)

  