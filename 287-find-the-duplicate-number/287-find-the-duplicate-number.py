class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            j=abs(nums[i])
            if(nums[j]<0):
                return j
            else:
                nums[j]=-nums[j]
                
            
        
        