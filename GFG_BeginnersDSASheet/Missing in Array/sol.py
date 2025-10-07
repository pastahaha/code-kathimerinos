class Solution:
    def missingNum(self, arr):
        # code here
        temp=0
        arrSum=0
        leng=len(arr)+2
        
        for x in range(1, leng, 1):
            temp ^= x
            
        for x in arr:
            arrSum ^= x
            
        return temp^arrSum 