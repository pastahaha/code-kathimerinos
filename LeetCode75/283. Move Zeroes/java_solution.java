class Solution {
    public int[] moveZeroes(int[] nums) {
        int leng=nums.length;
        int curr=0;

        for(int i=0;i<leng;i++){
            if (nums[i]!=0){
                nums[curr]=nums[i];
                curr++;
            }
        }

        for(int i=curr;i<leng;i++){
            nums[i]=0;
        }

        return nums;
    }
}