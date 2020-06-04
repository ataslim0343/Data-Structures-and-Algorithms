'''
Given two numbers x and y, and a range [l, r] where 1 <= l, r <= 32. 
The task is consider set bits of y in range [l, r] and set these bits in x also.

For example, if x = 10, l = 2, r = 3, y = 13  the program should change x to 14. 
Binary representation of 10 is 1010 and that of y is 1101. There is one set bit in y at 3’rd position 
(in given range). After we copy this bit to x, x becomes 1110 which is binary representation of 14.

'''


for t in range(int(input())):
    x,l,r,y=map(int,input().split())
    for i in range(l-1,r):
        if(y&1<<i):
            x|=(1<<i)
    print(x)
        
    
    
    
    
    
