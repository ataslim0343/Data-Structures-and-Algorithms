class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=set(nums)
        for i in s:
            if nums.count(i)>n//2:
                return i
                break
        