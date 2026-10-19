class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana={}
        
        if len(s)!=len(t):
            return False
        for char in s:
            if char not in ana:
                ana[char]=1
            else:
                ana[char]+=1
            
        for char in t:
            if char in ana and ana[char]>0:
                ana[char]=ana[char]-1
            else:
                return False
        return True