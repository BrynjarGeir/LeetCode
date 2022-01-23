from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return None
        pre_head = ListNode(-1)
        pre_head.next = head
        nxt = pre_head
        
        while nxt.next != None:
            if nxt.next.val == val:
                nxt.next = nxt.next.next
            else: nxt = nxt.next
        
        return pre_head.next