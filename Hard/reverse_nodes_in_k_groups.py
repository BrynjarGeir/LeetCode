# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, nxt = 0, head
        while nxt and count < k:
            nxt = nxt.next
            count += 1
        if count < k: return head
        
        nhead, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(nhead, k)
        return prev
    
    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return cur, prev