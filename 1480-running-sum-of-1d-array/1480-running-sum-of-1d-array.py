class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
      
        resultList=[0]*len(nums)
        resultList[0]=nums[0]
        for i in range(1,len(nums)):
            resultList[i]=resultList[i-1]+nums[i]
        return resultList