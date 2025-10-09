class Solution {
    public boolean increasingTriplet(int[] nums) {
        float first=Float.POSITIVE_INFINITY;
        float second=Float.POSITIVE_INFINITY;
        for(int i=0;i<nums.length;i++){
            if(nums[i]<=first){
                first=nums[i];
            }
            else if(nums[i]<=second){
                second=nums[i];
            }
            else{
                return true;
            }
        }
        return false;
    }
}