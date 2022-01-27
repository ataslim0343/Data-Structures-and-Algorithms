class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        # total_sum=(n*(n+1))//2
        # return total_sum-sum(nums)
        
        ans=0
        for i in range(n):
            ans^=(i+1)
            ans^=nums[i]
        return ans
        