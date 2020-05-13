# Find Numbers with Even Number of Digits (Leetcode Problem- 1295)

## Problem Statement-  Given an array nums of integers, return how many of them contain an even number of digits.

### Python Solution- Method 1

```
def findNumbers(nums):
    c=0
    for i in nums: #iterating through list
        n=i
        digitcount=0
        while(n>0):
            n=n//10
            digitcount+=1 
        if(digitcount%2==0):
            c=c+1
    return c
if __name__=="__main__":
    n=int(input())
    nums=list(map(int,input().split(",")))
    print(findNumbers(nums))
```
    
### Python Solution- Method 2

```
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            j=str(i)
            x=len(j)
            if x%2==0:
                c=c+1
        return c
```
