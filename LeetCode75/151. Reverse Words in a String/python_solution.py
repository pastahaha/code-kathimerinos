class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)
        sent = []
        i = 0

        while i < n:
            while i < n and s[i] == " ":
                i += 1
            if i == n: 
                break

            word=[]
            
            while i<n and s[i] != " ":
                word.append(s[i])
                i+=1 

            sent.append("".join(word))

        return " ".join(reversed(sent))