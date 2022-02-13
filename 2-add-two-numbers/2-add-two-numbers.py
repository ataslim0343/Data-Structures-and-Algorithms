# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3=ListNode(0)
        h3=l3
        c=0
        while(l1 or l2 or c):
            if l1:
                c+=l1.val
                l1=l1.next
            if l2:
                c+=l2.val
                l2=l2.next
            l3.val=c%10
            c=c//10
            if l1 or l2 or c:
                l3.next=ListNode(0)
                l3=l3.next
        return h3
        