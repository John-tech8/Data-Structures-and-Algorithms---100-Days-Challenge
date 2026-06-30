class Solution:
    def rotate(self, arr):
       n=len(arr)
       if n==0:
           return 
       
       arr[:]=arr[n-1:]+arr[:n-1]
      
