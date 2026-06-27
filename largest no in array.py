class Solution:
    def largestElement(self, nums):
        max_value=nums[0]
        for x in nums:
            if x>max_value:
                max_value=x
        print(max_value)
