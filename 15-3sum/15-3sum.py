class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        ans=set()
        n=len(nums)
#A[i]+A[left]+A[right]=0 ==>> A[left]+A[right] = 0-A[i] ==>> target = 0-A[i]
        for i in range(n-1):
            left=i+1
            right=n-1 
            target=0-nums[i]
            while(left<right):
                if nums[left]+nums[right]==target:
                    ans.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return list(ans)
                    
           
            
            