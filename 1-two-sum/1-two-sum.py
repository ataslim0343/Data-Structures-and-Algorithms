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
            if target-p in d.keys():
                res.append(d[target-p])
                res.append(i)
            else:
                d[p]=i
        return res
        