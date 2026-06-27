class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        k = k % n
        nums[:] = nums[k:] + nums[:k]