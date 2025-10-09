class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        ans = [1] * leng

        prefix = 1
        for i in range(leng):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(leng - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
