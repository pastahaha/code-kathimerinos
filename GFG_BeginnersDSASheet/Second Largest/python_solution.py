class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        lar=-1
        s_lar=-1
        
        for num in arr:
            if num>lar:
                s_lar=lar
                lar=num
            elif num<lar and num>s_lar:
                s_lar=num
            
        return s_lar