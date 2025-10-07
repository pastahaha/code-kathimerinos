#User function Template for python3
class Solution:

    def findMaximum(self, arr):
        # code here
        start=0
        end=len(arr)-1
        
        while start<=end:
            mid=(start+end)//2
            
            if mid>0 and mid<len(arr)-1:
            
                if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                    return arr[mid]
                    
                elif arr[mid]>arr[mid-1]:
                    start=mid+1
                    
                else:
                    end=mid-1
                
            elif mid == 0:
                if arr[0]>arr[1]:
                    return arr[0]
                else:
                    return arr[1]
                
            else:
                return max(arr[-1], arr[-2])