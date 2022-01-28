class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #return len(s.split()[-1])
        c=0
        flag=0
        for i in s[::-1]:
            if i!=" ":
                c+=1
                flag=1
            elif flag:
                break
        return c
        