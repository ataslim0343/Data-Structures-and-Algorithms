'''
Given an unsigned integer N. The task is to swap all odd bits with even bits. For example, if the given number is 23 (00010111), it should be converted to 43(00101011). Here, every even position bit is swapped with adjacent bit on right side(even position bits are highlighted in binary representation of 23), and every odd position bit is swapped with adjacent on left side.

Input:
The first line of input contains T, denoting the number of testcases. Each testcase contains single line.

Output:
For each testcase in new line, print the converted number.

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 100

Example:
Input:
2
23
2

Output:
43
1

Explanation:
Testcase 1: BInary representation of the given number; 00010111 after swapping 00101011.

'''



for t in range(int(input())):
    n=int(input())
    #The idea is to Left shift odd bits by 1 and Right Shift even bits by 1
    #0xaaaaaaaa is number having all its even bits set
    even=(n&0xaaaaaaaa)>>1
    #0x55555555 is number having all its odd bits set
    odd=(n&0x55555555)<<1
    #ans=even|odd i.e. we will perform bitwise OR. 
    print(even|odd)
    
