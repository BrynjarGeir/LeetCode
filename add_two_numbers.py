from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(); nxt = head
        keep = 0
        while l1 or l2 or keep != 0:
            nxt.next = ListNode(); nxt = nxt.next
            if l1 == None and l2 == None:
                curr = keep
            elif l1 == None:
                curr = l2.val + keep
                l2 = l2.next
            elif l2 == None:
                curr = l1.val + keep
                l1 = l1.next
            else:
                curr = l1.val + l2.val + keep
                l1 = l1.next; l2 = l2.next
            if curr >= 10:
                val = curr - 10; keep = 1
            else:
                val = curr; keep = 0
            nxt.val = val
        return head.next