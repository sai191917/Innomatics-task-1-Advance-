#Running sum of Array

class Solution:
    def runningSum(self, nums):
        result = []
        running_total = 0

        for n in nums:
            running_total += n
            result.append(running_total)

        return result
