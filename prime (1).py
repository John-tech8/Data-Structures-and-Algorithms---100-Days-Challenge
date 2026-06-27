class Solution:
    def isPrime(self, n):
        is_prime=True
        # code here
        if n==1 or n==0:
            is_prime=False
            return is_prime
        else:
            for i in range(2,n):
                if n%i !=0:
                    return is_prime
                else:
                    is_prime=False
                    return is_prime
                    