class Solution {
    int missingNum(int arr[]) {
        // code here
        int all=0;
        int arrSum=0;
        int leng=arr.length;
        
        for(int i=1;i<leng+2;i++){
            all ^= i;
        }
        
        for(int i=0;i<arr.length;i++){
            arrSum ^= arr[i];
        }
        
        return all^arrSum;
    }
}