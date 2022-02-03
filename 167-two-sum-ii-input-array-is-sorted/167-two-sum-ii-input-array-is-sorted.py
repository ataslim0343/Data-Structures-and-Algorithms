class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        n=len(numbers)
        res=[]
        for i in range(n):
            p=numbers[i]
            if target-p in d.keys():
                res.append(d[target-p])
                res.append(i+1)
            else:
                d[p]=i+1
        return res