# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            prev=None
            curr=head
            nextt=None
            while(curr):
                nextt=curr.next
                curr.next=prev
                prev=curr
                curr=nextt
            head=prev
            return head
        
        l1=reverseList(self,l1)
        l2=reverseList(self,l2)
        # print(l1)
        # print(l2)
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
        h3=reverseList(self,h3)
        return h3