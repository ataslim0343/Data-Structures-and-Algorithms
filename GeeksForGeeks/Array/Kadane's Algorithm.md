"""
# Problem Statement

## Kadane's Algorithm - (DP Approach)
### Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

User Task:
The task is to complete the function maxSubarraySum() which finds subarray with maximum sum.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input:
2
5
1 2 3 -2 5
4
-1 -2 -3 -4

Output:
9
-1

"""


# CODE - Python-3.x

```
def maxSubArraySum(a,size):
    #maximum_sum will store max subarray sum
    maximum_sum=-9999999
    #maximum_sum_till_i will store current sum
    maximum_sum_till_i=0
    for i in range(size):
        maximum_sum_till_i=max(a[i],maximum_sum_till_i+a[i])
        maximum_sum=max(maximum_sum,maximum_sum_till_i)
    return maximum_sum
```
