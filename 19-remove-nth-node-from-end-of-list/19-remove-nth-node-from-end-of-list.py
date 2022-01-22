# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # Time Complexity = O(2n)
        temp=head
        c=0
        while(temp):
            c+=1
            temp=temp.next
        curr=head
        if(c==n):
            return head.next
        for i in range(c-n-1):
            curr=curr.next
        curr.next=curr.next.next
        return head
        