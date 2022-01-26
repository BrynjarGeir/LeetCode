# This one seems to have gone well. Faster than 94.34% and less memory than 85.82%
from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: return None
        elif list1 == None: return list2
        elif list2 == None: return list1
        else:
            if list1.val <= list2.val: 
                head = list1; list1 = list1.next
            else:
                head = list2; list2 = list2.next
        nxt = head
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    nxt.next = list1
                    nxt = nxt.next
                    list1 = list1.next
                else:
                    nxt.next = list2
                    nxt = nxt.next
                    list2 = list2.next
            elif list1 == None:
                nxt.next = list2
                return head
            else:
                nxt.next = list1
                return head
        return head