class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        i=0
        op=[]
        while i != len(candies):
            curr=candies[i]+extraCandies
            op.append(self.checkMax(curr,candies))
            i+=1
        return op

    def checkMax(self, curr, candies):
        for x in candies:
            if curr < x:
                return False
        return True