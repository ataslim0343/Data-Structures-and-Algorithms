class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]"""
        
        n=len(nums)
        res=[0]*(2*n)
        for i in range(n):
            res[i]=nums[i]
            res[i+n]=nums[i]
        return res
        