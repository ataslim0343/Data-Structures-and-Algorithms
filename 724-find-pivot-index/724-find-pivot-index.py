class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==1):
            return 0
        if(n==2):
            return -1
        total_sum=sum(nums)
        left_sum,right_sum=0,total_sum
        for i in range(n):
            right_sum-=nums[i]
            if(right_sum==left_sum):
                return i
            left_sum+=nums[i]
        return -1