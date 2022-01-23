from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: return
        nxt = head
        while nxt:
            while nxt.next and nxt.val == nxt.next.val:
                nxt.next = nxt.next.next
            nxt = nxt.next
        return head