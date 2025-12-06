# Shuffle the Array
class Solution:
    def shuffle(self, nums, n):
        combined = []
        for k in range(n):
            x_val = nums[k]
            y_val = nums[k + n]
            combined.append(x_val)
            combined.append(y_val)
        return combined
