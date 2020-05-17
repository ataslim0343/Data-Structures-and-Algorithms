# Union of Two Sorted Arrays
## Given two sorted arrays arr[] and brr[] of size N and M respectively. The task is to find the union of these two arrays.
## Union of two arrays can be defined as the common and distinct elements in the two arrays.

### Input:
First line of input contains number of testcases T. For each testcase, first line of input contains number of testcases T. For each testcase, first line of input contains size of two arrays N and M. Next two line contains N and M elements.

### Output:
For each testcase, print the union (common and distinct) of two arrays in a single line. You need to print the union in sorted order.

### Your Task:
This is a function problem. You only need to complete the function findUnion() that takes N and M as parameter and prints the union of two arrays. The newline is automatically appended by the driver code.

### Constraints:<br>
1 <= T <= 100<br>
1 <= N, M <= 105<br>
1 <= arr[i], brr[i] <= 106<br>

### Example:
#### Input:<br>
3<br>
5 3<br>
1 2 3 4 5<br>
1 2 3<br>
5 5<br>
2 2 3 4 5<br>
1 1 2 3 4<br>
5 5<br>
1 1 1 1 1<br>
2 2 2 2 2<br>

#### Output:<br>
1 2 3 4 5<br>
1 2 3 4 5<br>
1 2<br>

#### Explanation:<br>
Testcase 1: Distinct elements including both the arrays are: 1 2 3 4 5.<br>
Testcase 2: Distinct elements including both the arrays are: 1 2 3 4 5.<br>
Testcase 3: Distinct elements including both the arrays are: 1 2.<br>
 
 
 ```
 def mergeArrays(a,b,n,m):
    newArray=[]
    i=j=0
    while(i<n and j<m):
        #Handling duplicate elements in first array
        while(i<n-1 and a[i]==a[i+1]):
            i+=1
        #Handling duplicate elements in second array
        while(j<m-1 and b[j]==b[j+1]):
            j+=1
        #If elemnt in first array is less then insert it in new array
        if(a[i]<b[j]):
            newArray.append(a[i])
            i+=1
        #If elemnt in second array is less then insert it in new array
        elif(a[i]>b[j]):
            newArray.append(b[j])
            j+=1
        #If elemnt in both array are same then insert anyone of them
        # in new array
        else:
            newArray.append(a[i])
            i+=1
            j+=1
    #Checking if any element is left in first array
    while(i<n):
        #Here again checking for duplicates
        if(i<n-1 and a[i]==a[i+1]):
            i+=1
        #If not duplicate, inserting in new array
        else:
            newArray.append(a[i])
            i+=1
    #Checking if any element is left in second array
    while(j<m):
        #Here again checking for duplicates
        if(j<m-1 and b[j]==b[j+1]):
            j+=1
        #If not duplicate, inserting in new array
        else:
            newArray.append(b[j])
            j+=1
            
    for i in newArray:
        print(i, end=" ")
  ```
