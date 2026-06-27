class Solution:
    def search(self, arr, x):
        ElementFound=False
        for i in range(len(arr)):
            if arr[i]==x:
                return i
                
        if not ElementFound:
            return -1
