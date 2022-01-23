from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nxt = head; seen = [head]
        while nxt:
            if nxt.next in seen: return True
            else:
                seen.append(nxt.next)
                nxt = nxt.next
        return False
##or this, above is mine
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow, fast = head, head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False