class Solution:
    def reverseexponentiation(self, n):
        strings=str(n)
        strings=strings[::-1]
        strings=int(strings)
        return n**strings
