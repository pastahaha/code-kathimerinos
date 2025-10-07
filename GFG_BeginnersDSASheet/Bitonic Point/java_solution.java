// User function Template for Java

class Solution {
    public int findMaximum(int[] arr) {
        // code here
        int leng=arr.length;
        int start=0;
        int end=leng-1;
        
        while(start<=end){
            int mid = (start+end)/2;
            
            if (mid>0 && mid<leng){
                
                if((arr[mid]>arr[mid-1]) && (arr[mid+1]<arr[mid])){
                    return arr[mid];
                }
                
                else if((arr[mid]>arr[mid-1]) && (arr[mid+1]>arr[mid])){
                    start=mid+1;
                }
                else{
                    end=mid-1;
                }
            }
            
            else if(mid==0){
                return (arr[0]>arr[1]) ? arr[0] : arr[1];
            }
            
            else{
                return (arr[leng-1]>arr[leng-2])?arr[leng-1]:arr[leng-2];
            }
            
        }
        return -1;
    }
}