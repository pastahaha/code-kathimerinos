class Solution:
    def compress(self, chars: List[str]) -> int:
        left=0
        right=0
        leng=len(chars)
        while right<leng:
            char = chars[right]
            count=0

            while right<leng and chars[right] == char:
                right+=1
                count+=1

            chars[left]=char
            left+=1

            if count>1:
                for digit in str(count):
                    chars[left]=digit
                    left+=1
        return left
