class Solution:
    def get_min_max(self, arr):
        min=float('inf')
        max=float('-inf')
        for x in range (len(arr)):
            if arr[x]<min:
                min=arr[x]
            if arr[x]>max:
                max=arr[x]
                
        return [min, max]