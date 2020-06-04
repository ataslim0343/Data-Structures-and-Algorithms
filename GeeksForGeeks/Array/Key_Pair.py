#Given an array A of N positive integers and another number X. 
#Determine whether or not there exist two elements in A whose sum is exactly X.

#Code- Considering Dupliate Elements as well

for t in range(int(input())):
    n,x=map(int,input().split())
    arr=[int(i) for i in input().split()]
    flag=0
    for i in range(n):
				#x=arr[i] + k ==>> if k is in array then the pair exist.
        k=x-arr[i]
        if k in arr and arr.index(k)!=i:
            flag=1
            break
    if(flag==1):
        print("Yes")
    else:
        print("No")
            
    
    
