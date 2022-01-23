from typing import ListNode, Optional
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB: return None
        nxtA = headA; nxtB = headB
        while nxtA is not nxtB:
            nxtA = headB if nxtA is None else nxtA.next
            nxtB = headA if nxtB is None else nxtB.next
        return nxtA