'''
You are given an array A[] of size N. Now, we call the value of an array the bit-wise XOR of all elements it contains. For example, the value of the array [1,2,3] = 1^2^3. Now, Your task is to find the bit-wise XOR of the values of all sub arrays of array A. 

Example:

Input: A[] = {1,2,3} 
Output: 2
xor[1] = 1, 
xor[1, 2] = 3
xor[2, 3] = 1
xor[1, 2, 3] = 0
xor[2] = 2
xor[3] = 3
Result : 1 ^ 3 ^ 1 ^ 0 ^ 2 ^ 3 = 2


'''

#code
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    '''
    #It is observed that if n is even XOR(all subArrays of array)=0
    #If n is odd, XOR(all subArrays of array)=XOR(alternate elements of-
    # -array starting from 0th index.)
    #If arr=[1,2,3]==>> ans=2 as n is odd and (1^3)=2
    #If arr=[1,2,3,4]==>> ans=0 as n is even
    #If arr=[1,2]==>>ans=0 as n is even
    #If arr=[5,6,7]==>>ans=2 as n is odd and (5^7)=2
    '''
    
    ans=0
    if(n%2==0):
        ans=0
    else:
        for i in range(0,n,2):
            ans=ans^arr[i]
    print(ans)
        
