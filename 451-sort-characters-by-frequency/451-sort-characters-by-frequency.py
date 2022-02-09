class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_dict=sorted(d.items(),key=lambda item:item[1],reverse=True)
        ans=""
        #print(sorted_dict)
        for i, j in sorted_dict:
            ans+=i*j
        return ans
        