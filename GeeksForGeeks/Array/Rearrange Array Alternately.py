'''

Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e 
first element should be max value, second should be min value, third should be second max, fourth should 
be second min and so on...
Input:
2
6
1 2 3 4 5 6
11 
10 20 30 40 50 60 70 80 90 100 110

Output:
6 1 5 2 4 3
110 10 100 20 90 30 80 40 70 50 60


'''


# Solution 1--- Time = O(n) & Space =O(n)

for i in range(int(input())):
    n=int(input())
    arr=list(input().split())
    for i in range(n):
        arr[i]=int(arr[i])
    ans=[0]*n
    k=0
    for i in range(1,n,2):
        ans[i]=arr[k]
        k+=1
    p=n-1
    for j in range(0,n,2):
        ans[j]=arr[p]
        p-=1
    print(*ans)
        
   
# Solution 1--- Time = O(n) & Space =O(1)

for t in range(int(input())):
    n=int(input())
    arr=list(input().split())
    for p in range(n):
        arr[p]=int(arr[p])
    minn=0
    maxx=n-1
    z=arr[n-1]+1
    for i in range(0,n):
        if i%2==0:
            arr[i]+=(arr[maxx]%z)*z
            maxx-=1
        else:
            arr[i]+=(arr[minn]%z)*z
            minn+=1
    for j in range(n):
        print(arr[j]//z, end=" ")


 
