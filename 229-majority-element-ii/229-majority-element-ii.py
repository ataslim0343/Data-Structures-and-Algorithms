class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        n=len(nums)
        s=set(nums)
        for i in s:
            if nums.count(i)>n//3:
                ans.append(i)
        return ans
        