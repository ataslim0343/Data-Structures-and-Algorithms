class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        return (" ".join(reversed(l))).strip()