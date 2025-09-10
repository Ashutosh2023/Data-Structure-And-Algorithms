class Solution:
    @staticmethod
    def getPrimeFactorsSum(n: int) -> int:
        pFactors = []
        for i in range(2, math.isqrt(n)+1):
            if i>=math.isqrt(n)+1:
                break
            if n % i == 0:
                while n%i==0:
                    pFactors.append(i)
                    n = n//i
        if(n!=1):
            pFactors.append(n)
        return sum(pFactors)

    def smallestValue(self, n: int) -> int:
        while True:
            sum = Solution.getPrimeFactorsSum(n)
            if(n == sum):
                break
            n = sum
        return n