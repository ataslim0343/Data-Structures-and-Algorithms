class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binN(N):
            s=""
            while(N):
                s=str(N%2)+s
                N=N//2
            return s
        comp_s=""
        if n==0:
            return 1
        for i in binN(n):
            if i=='0':
                comp_s+='1'
            else:
                comp_s+='0'
        return int(comp_s,2)
        