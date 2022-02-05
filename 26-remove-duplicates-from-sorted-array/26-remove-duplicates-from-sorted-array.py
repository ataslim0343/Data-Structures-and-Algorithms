class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if(n==0 or n==1):
            return n
        j=0
        for i in range(n-1):
            if(nums[i] != nums[i+1]):
                nums[j]=nums[i]
                j+=1
        nums[j]=nums[n-1]
        j=j+1
        return j
        