# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = []; nxt = head
        while nxt:
            ans.append(str(nxt.val))
            nxt= nxt.next
        ans = ''.join(ans)
        return int(ans, 2)