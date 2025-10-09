class Solution {
    public int[] productExceptSelf(int[] nums) {
        int leng = nums.length;
        int[] ans = new int[leng];
        ans[0]=1;
        for(int i=1; i<leng;i++){
            ans[i]=nums[i-1]*ans[i-1];
        }

        int suffix = 1;
        for(int i=leng-1; i>=0;i--){
            ans[i]=ans[i]*suffix;
            suffix*=nums[i];
        }
        return ans;
    }
}