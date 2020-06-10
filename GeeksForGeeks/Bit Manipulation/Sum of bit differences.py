'''
Write a program to find the sum of bit differences in all pairs that can be formed from array elements n. Bit difference of a pair (x, y) is a count of different bits at same positions in binary representations of x and y. For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111 ( first and last bits differ in two numbers).
 

Input: The first line of input contains an integer T denoting the number of test cases. First line of the test case will contain an array of elements n.

Output: The sum of bit differences of all pairs that can be formed by given array.

Constraints:

1 <=T<= 100

1 <=N<= 10

1 <=a[i]<= 10

Example:

Input:
2
2 
1 2
3 
1 3 5

Output:
4
8

Note: (a, b) and (b, a) are considered two separate pairs.

Explanation:
Test Case 1: 
1: 01
2: 10
Bit difference in pair (1, 2): 2
Bit difference in pair (2, 1): 2
Hence, total Bit difference = 2 + 2 = 4

Test Case 2: 
1: 001
3: 011
5: 101
Bit difference in pair (1, 3): 1
Bit difference in pair (3, 1): 1
Bit difference in pair (1, 5): 1
Bit difference in pair (5, 1): 1
Bit difference in pair (3, 5): 2
Bit difference in pair (5, 3): 2
Hence, total Bit difference = 1+1+1+1+2+2 = 8. 

'''

1. Naive Approach - O(n*n)

for testcases in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    #O(n*n) Solution
    ans=0
    for i in range(n-1):
         for j in range(i+1,n):
    #The idea is find XOR of numbers in a pair and then count no of 1's
    #and multiply the count by 2 bcoz (x,y) and (y,x) are 
    #considered two different pairs
             x=arr[i]^arr[j]
             x=bin(x)[2:]
             ans+=x.count('1')
     print(ans*2)
     
     
     
 2. Optimized Approach- O(32*n)
 
 for testcases in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=0
    for i in range(32):
        #to count number of elements with ith bit set.
        count=0
        for j in range(n):
            if((arr[j] & (1<<i))):
                count+=1
        #to find all permutations count
        #count = no of set bits
        # n-count = no of unset bits
        # 2*(count)*(n-count) = permutations of all counts
        ans+=(count*(n-count)*2)
    print(ans)
        
            
            
