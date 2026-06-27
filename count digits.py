class Solution:
    def evenlyDivides(self, n):
        # code here
        count=0
        k=str(n)
        for s in k:
            digit=int(s)
            if digit!=0 and n% digit==0:
                count+=1
        return  count
                
