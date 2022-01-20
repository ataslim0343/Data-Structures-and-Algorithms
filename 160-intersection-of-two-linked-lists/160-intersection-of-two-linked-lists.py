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
        n1,n2=0,0
        curr1,curr2=headA,headB
        while(curr1):
            n1+=1
            curr1=curr1.next
        while(curr2):
            n2+=1
            curr2=curr2.next
        temp1,temp2=headA,headB
        if(n1>=n2):
            for i in range(n1-n2):
                temp1=temp1.next
            while(temp1!=temp2):
                temp1=temp1.next
                temp2=temp2.next
            return temp1
        else:
            for i in range(n2-n1):
                temp2=temp2.next
            while(temp1!=temp2):
                temp1=temp1.next
                temp2=temp2.next
            return temp1
        return None
        
        