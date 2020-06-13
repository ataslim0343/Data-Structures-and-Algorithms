'''

Given a binary string S. The task is to count the number of substrings that start and end with 1. 
For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

'''

Hint- Count number of 1's (let say count_1) in string
      resut will be count_1C2 i.e. (count_1)*(count_1-1)//2
      
Python Code-



for i in range(int(input())):
    n=int(input())
    s=input()
    count_1=0
    for i in range(n):
        if s[i]=="1":
            count_1+=1
    #Count number of 1's (let say count_1) in string
    #resut will be count_1C2 i.e. (count_1)*(count_1-1)//2
    result=(count_1)*(count_1-1)//2
    print(result)
            
    
