class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        n=len(nums)
        res=[]
        for i in range(n):
            p=nums[i]
            if p in d.keys():
                res.append(d[p])
                res.append(i)
            else:
                d[target-p]=i
        return res
        