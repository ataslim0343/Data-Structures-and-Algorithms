# Median of Two sorted arrays
## Given two sorted arrays arr[] and brr[] of sizes N and M respectively. The task is to find the median of the two arrays when they get merged.

### Input Format:
First line of input contains number of testcases T. First line of input contains number of elements in both arrays N and M respectively. Next two lines contains the array elements.

### Output Format:
For each testcase, in a new line, print the median.

### Your Task:
Complete findMedian function and return the median of two sorted arrays. If there are total even elements, we need to return floor of average of middle two elements.

#### Constraints:<br>
1 <= T <= 100<br>
1 <= N, M <= 106<br>
1 <= arr[i], brr[i] <= 107<br>

### Example:<br>
#### Input:<br>
4<br>
5 6<br>
1 2 3 4 5<br>
3 4 5 6 7 8<br>
2 3<br>
1 2<br>
2 3 4<br>
4 4<br>
1 2 3 4<br>
11 12 13 14<br>
4 3<br>
1 2 3 4<br>
2 3 4<br>

#### Output:<br>
4<br>
2<br>
7<br>
3<br>

#### Explanation:
Testcase 1: After merging two arrays, elements will be as 1 2 3 3 4 4 5 5 6 7 8. So, median is 4.<br>
Testcase 2: After merging two arrays, elements will be as 1 2 2 3 4. So, median is 2.<br>
Testcase 3: After merging two arrays, elements will be as 1 2 3 4 11 12 13 14. So, median is (4+11)/2=7.<br>
Testcase 4: After merging two arrays, elements will be as 1 2 2 3 3 4 4. So, median is 3.<br>

```

def findMedianSortedArrays(arr1, n, arr2, n2):
    #newArray will be obtained after merging two sorted array
    newArray=[0]*(n+n2)
    #Merging two sorted arrays into one sorted array
    i=j=k=0
    while(i<n and j<n2):
        if arr1[i]<=arr2[j]:
            newArray[k]=arr1[i]
            i+=1
            k+=1
        else:
            newArray[k]=arr2[j]
            j+=1
            k+=1
    while(i<n):
        newArray[k]=arr1[i]
        i+=1
        k+=1
    while(j<n2):
        newArray[k]=arr2[j]
        j+=1
        k+=1
    # print(newArray)
    newArrayLen=len(newArray)
    if(newArrayLen%2==0):
        mid=newArrayLen//2
        #Finding median in case if size of array is even
        #if newArrayLen=8 , mid=4, median will be average 
        #of 4th and 5th elment.
        #Due to zero indexing we are finding avg of arr[mid-1] and arr[mid] 
        median=(newArray[mid-1]+newArray[mid])//2
        return median
    else:
        mid=(newArrayLen+1)//2
        #since index is from 0,so returning arr[mid-1].
        median=newArray[mid-1] 
        return median
        
  ```
