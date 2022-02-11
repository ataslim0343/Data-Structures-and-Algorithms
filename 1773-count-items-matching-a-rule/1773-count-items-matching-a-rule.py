class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleKeys={"type":0,"color":1,"name":2}
        c=0
        for i in items:
                if i[ruleKeys[ruleKey]]==ruleValue:
                    c+=1
        return c
        