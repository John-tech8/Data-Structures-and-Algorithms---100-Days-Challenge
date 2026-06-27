class Solution:
    def secondLargestElement(self, nums):
        largest_value=nums[0]
        sLargest=-1
        for number in nums:
            if number> largest_value:
                sLargest=largest_value
                largest_value=number
            elif number<largest_value and number>sLargest:
                sLargest=number
        return sLargest
