# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        str1=""
        str2=""
        while(head):
            str1+=str(head.val)
            str2=str(head.val)+str2
            head=head.next
        if(str1==str2):
            return True
        else:
            return False
        
        