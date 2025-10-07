class Solution:
    def search(self, arr, x):
        # code here
        for num in range(len(arr)):
            if arr[num]==x:
                return num
        return -1