class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
            
        leng = len(flowerbed)

        for i in range(leng):
            if flowerbed[i]==0 and ((i==0) or (flowerbed[i-1]==0)) and ((i==leng-1) or (flowerbed[i+1]==0)):
                    flowerbed[i]=1
                    n-=1
                    if n==0:
                        return True
        return False