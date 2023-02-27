class Solution:
    results = {}
    def climbStairs(self, n: int) -> int:
        if n in Solution.results:
            return Solution.results[n]
        elif n < 3:
            return n
        else:
            r = self.climbStairs(n-2) + self.climbStairs(n-1)
            Solution.results[n] = r
            return r