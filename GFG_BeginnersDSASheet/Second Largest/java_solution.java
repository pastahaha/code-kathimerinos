class Solution {
    public int getSecondLargest(int[] arr) {
        // code here
        int lar = -1;
        int s_lar = -1;
        
        for(int i=0; i<arr.length; i++){
            if(arr[i]>lar){
                s_lar=lar;
                lar=arr[i];
            }
            
            else if(arr[i]<lar && arr[i]>s_lar){
                s_lar=arr[i];
            }
        }
        return s_lar;
    }
}