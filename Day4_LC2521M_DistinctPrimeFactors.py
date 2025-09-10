class Solution:
    @staticmethod
    def getPrimeFactors(n: int, factors: set):
        for i in range(2, math.isqrt(n)+1):
            if i>=math.isqrt(n)+1:
                break
            if n % i == 0:
                factors.add(i)
                while n%i==0:
                    n = n//i
        if(n!=1):
            factors.add(n)

    def distinctPrimeFactors(self, nums: List[int]) -> int:
        factors = set()
        for item in nums:
            Solution.getPrimeFactors(item, factors)
        return len(factors)