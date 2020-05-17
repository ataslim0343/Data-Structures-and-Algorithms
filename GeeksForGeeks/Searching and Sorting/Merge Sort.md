# Merge Sort
## The task is to complete merge() function which is used to implement Merge Sort.

### Input:
First line of the input denotes number of test cases 'T'. First line of the testcase is the size of array and second line consists of array elements separated by space.

### Output:
Sorted array in increasing order is displayed to the user.

### User Task:
Since this is a functional problem you don't have to worry about input, you just have to complete the function merge().

### Constraints:<br>
1 <= T <= 50<br>
1 <= N <= 105<br>
1 <= arr[i] <= 103<br>

### Example:<br>
#### Input:<br>
2<br>
5<br>
4 1 3 9 7<br>
10<br>
10 9 8 7 6 5 4 3 2 1<br>

#### Output:<br>
1 3 4 7 9<br>
1 2 3 4 5 6 7 8 9 10<br>

### Explanation:<br>
Testcase 1: The array after performing mergesort is: 1 3 4 7 9.<br>


```

def mergeSort(arr):
    n=len(arr)
    if(n<2):
        return 
    m=n//2
    #divind array into two halves
    L=arr[0:m]
    R=arr[m:]
    #sorting first half
    mergeSort(L)
    #sorting second half
    mergeSort(R)
    i=j=k=0
    #Merging the sorted array
    while(i<len(L) and j<len(R)):
        if(L[i]<R[j]):
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1
    #Checking if any element is left in left half
    while(i<len(L)):
        arr[k]=L[i]
        i+=1
        k+=1
   #Checking if any element is left in right half
    while(j<len(R)):
        arr[k]=R[j]
        j+=1
        k+=1
    return arr
            





```
