# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited=set()
        curr1,curr2=headA,headB
        while(curr1):
            visited.add(curr1)
            curr1=curr1.next
        while(curr2):
            if curr2 in visited:
                return curr2
            curr2=curr2.next
        return None
        