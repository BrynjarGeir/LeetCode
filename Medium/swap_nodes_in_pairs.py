from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, prev.next = self, head
        while prev.next and prev.next.next:
            curr = prev.next
            nxt = prev.next.next
            prev.next, nxt.next, curr.next = nxt, curr, nxt.next
            prev = curr
        return self.next