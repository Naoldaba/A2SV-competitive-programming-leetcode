class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        li=[i for i in s]
        for j in t:
            if j in li:
                li.remove(j)
            else:
                return False
        if len(li)==0:
            return True
