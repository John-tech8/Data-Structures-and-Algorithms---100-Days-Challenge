class Solution:
    def thirdLargest(self, arr):
        first = second = third = float('-inf')

        for num in arr:
            if num > first:
                third = second
                second = first
                first = num
            elif first > num > second:
                third = second
                second = num
            elif second > num > third:
                third = num

        return third