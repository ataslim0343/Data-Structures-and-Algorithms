class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        n=len(nums)
        k=k%n
        nums[:]=reversed(nums)
        nums[:k],nums[k:]=reversed(nums[:k]),reversed(nums[k:])
        