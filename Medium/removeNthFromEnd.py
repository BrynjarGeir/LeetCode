# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end, nth = head, head
        for i in range(n):
            end = end.next
        while end is not None and end.next is not None:
            end = end.next
            nth = nth.next
        if end is not None:
            nth.next = nth.next.next
        else:
            head = head.next
        return head
        
        