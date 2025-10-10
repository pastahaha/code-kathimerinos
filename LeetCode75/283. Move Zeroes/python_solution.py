class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr=0
        leng=len(nums)
        for x in range(leng):
            if nums[x] != 0:
                nums[curr]=nums[x]
                curr+=1

        for i in range(curr, leng):
            nums[i] = 0

        return nums        