#Given an array of integers, and an integer  ‘K’ , \
#find the count of pairs of elements in the array whose sum is equal to 'K'.


from collections import Counter
def countPairs(arr,n,k):
    d=Counter(arr)
    count=0
    for i in arr:
        j=k-i #(Since i+j=k => j=k-1)
        if j in d:
            if j==i: #(Checking if i+i=k)
                count+=d[j]-1
            else:
                count+=d[j]
    #count//2 bcoz of duplicacy
    return (count//2)
        
for i in range(int(input())):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    print(countPairs(arr,n,k))
    
