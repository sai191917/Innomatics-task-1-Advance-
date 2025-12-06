# Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        return [(c + extraCandies) >= m for c in candies]
