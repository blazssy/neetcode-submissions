class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else:
            for i in range(len(s)):
                if Counter(s)==Counter(t):
                    return True  
                else:
                    return False      