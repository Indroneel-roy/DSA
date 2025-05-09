# Problem Link : https://leetcode.com/problems/reorder-list/description/
from typing import Optional, List

# Definition for singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Split the list
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

# Helper: Convert list to linked list
def list_to_linkedlist(items: List[int]) -> Optional[ListNode]:
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper: Print linked list
def print_linkedlist(head: Optional[ListNode]) -> None:
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()

# Test
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = list_to_linkedlist(arr)
    print("Original list:")
    print_linkedlist(head)

    sol = Solution()
    sol.reorderList(head)

    print("Reordered list:")
    print_linkedlist(head)
