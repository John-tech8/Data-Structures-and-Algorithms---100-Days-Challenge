from collections import Counter

class Solution:
    def frequencyCount(self, arr):
        n = len(arr)
        # Count frequencies of all elements in the array
        counts = Counter(arr)
        
        # GeeksforGeeks usually expects the original array to be modified in-place
        for i in range(n):
            # i + 1 because the numbers range from 1 to n
            arr[i] = counts[i + 1]
            
        return arr
