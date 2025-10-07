class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        leng=len(s)-1
        vow=set("aeiouAEIOU")
        s_list=list(s)
        while i < leng:
            if s_list[i] in vow and s_list[leng] in vow:
                s_list[i], s_list[leng] = s_list[leng], s_list[i]
                i += 1
                leng -= 1
            elif s_list[i] not in vow:
                i += 1
            elif s_list[leng] not in vow:
                leng -= 1
        return "".join(s_list)