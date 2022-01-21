class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        temp=int(num**0.5)
        return num==temp*temp
        