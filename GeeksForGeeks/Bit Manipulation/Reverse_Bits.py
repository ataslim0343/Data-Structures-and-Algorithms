'''
Given a 32 bit number x, reverse its binary form and print the answer in decimal.

Input:
The first line of input consists T denoting the number of test cases. T testcases follow. Each test case contains a single 32 bit integer

Output:
For each test case, in a new line, print the reverse of integer.

Constraints:
1 <= T <= 100
0 <= x <= 4294967295

Example:
Input:
2
1
5
Output:
2147483648
2684354560

'''


#Solution

for i in range(int(input())):
    n=int(input())
    bit_pos=31
    res=0
    while(n):
        #Checking if right bit is set
        if(n&1):
            res|=1<<bit_pos
            #The above expression is equivalent to
            #res+=pow(2,bit_pos) as bitwise OR is equivalent to sum
            #and pow(2,k) ==>> left shift of 1 by k times.==>>1*2^k
        bit_pos-=1
        #Discarding LSB of n or we can say that discarding MSB of reversed 
        #binary representation of n
        n>>=1
    print(res)
            
    
