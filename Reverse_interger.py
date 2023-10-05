class Solution:
    def reverse(self, x: int) -> int:
        if (-2**31<x<2**31-1):
            res=0
            if x==0:
                return 0
            elif x>0:
                while x>0:
                    dig=x%10
                    res=(res*10)+dig
                    x//=10
                if (-2**31<res<2**31-1):
                    return res
                return 0
            elif x<0:
                x=-x
                while x>0:
                    dig=x%10
                    res=(res*10)+dig
                    x//=10
                if (-2**31<res<2**31-1):
                    return -res
                return 0
        return 0
