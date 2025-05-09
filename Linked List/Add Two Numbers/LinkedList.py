# Problem Link : https://leetcode.com/problems/add-two-numbers/description/
from typing import List, Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper to print the list (for testing)
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return ' -> '.join(result)
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            # get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            #sum opreation and define carry and value
            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            #update the value
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next    

def create_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for number in lst:
        current.next = ListNode(number)
        current = current.next
    return dummy.next

if __name__ == "__main__":
    # Test case
    l1 = create_linked_list([2, 4, 3])  # represents 342
    l2 = create_linked_list([5, 6, 4])  # represents 465    
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)  # should return a list representing 807: [7, 0, 8]

    print("Result:", result)  # Output: 7 -> 0 -> 8