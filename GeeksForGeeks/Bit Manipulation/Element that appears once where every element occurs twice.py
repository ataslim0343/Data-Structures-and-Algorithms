'''
Given an array of integers, every element appears twice except for one. Find that single one in linear time complexity and without using extra memory.

Input:
The first line of input consists number of the test cases. The description of T test cases is as follows:
The first line of each test case contains the size of the array, and the second line has the elements of the array.

Output:
In each separate line print the number that appears only once in the array.

Constraints:
1 ≤ T ≤ 70
1 ≤ N ≤ 100
0 ≤ A[i] ≤ 100000

Example:
Input:
1
11
1 2 4 3 3 2 5 6 1 6 5
Output:
4

'''

#Solution--

for t in range(int(input())):
    n=int(input())
    ans=0
    arr=[int(i) for i in input().split()]
    for i in arr:
        #Elements occuring twice will becomes 0 and 0^A=A where A is 
        #Element occuring once.
        ans^=i
    print(ans)
    
