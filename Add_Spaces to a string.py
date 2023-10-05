class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        final = ""
        lastIdx = 0
        for i in spaces:
            final += s[lastIdx:i]
            final += " "
            lastIdx = i
        final += s[lastIdx:]
        return(final)
