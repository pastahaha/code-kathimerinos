class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        leng=len(s)
        i=0
        it=0
        while it<leng and i<len(t):
            if t[i] == s[it]:
                it+=1
            i+=1

        if it == leng:
            return True
        else:
            return False