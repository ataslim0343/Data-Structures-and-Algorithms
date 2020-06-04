#Given an array A of N positive integers and another number X. 
#Determine whether or not there exist two elements in A whose sum is exactly X.


#Explanation -

'''
Given arr=[2,3,4,5] and x=9
suppose there is a pair (a,b) such that a+b=x, it implies that b=x-a given that a!=b.
Note - If there are duplicate elements in array then index(a)!=index(b).
We are using the same idea here in the solution below.

'''

#Code- Considering Dupliate Elements as well

for t in range(int(input())):
    n,x=map(int,input().split())
    arr=[int(i) for i in input().split()]
    flag=0
    for i in range(n):
        k=x-arr[i]
        if k in arr and arr.index(k)!=i:
            flag=1
            break
    if(flag==1):
        print("Yes")
    else:
        print("No")


            
    
    
