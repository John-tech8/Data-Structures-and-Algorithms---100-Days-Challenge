class Solution:
    def floorSqrt(self, n): 
        # code here
        x=n//2
        tolerance=1e-6
        while True:
            root=0.5*(x+n/x)
            if abs(root-x)<tolerance:
                return round(root)
            x=root
            