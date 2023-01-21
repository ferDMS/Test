# Solution code for
# 53. Maximum Subarray.

from typing import List
import random
import pyperclip

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here, max_so_far = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

solution = Solution()
testcases = [
    [-2,1,-3,4,-1,2,1,-5,4],  # ans = 6
    [1],  # ans = 1
    [5,4,-1,7,8],  # ans = 23
    [random.randint(-100, 100) for i in range(1, 100)]
]

# pyperclip.copy(str(testcases[-1]))
for i in range(len(testcases)):
    print(f"\nCase #{i+1}:\n{testcases[i]}\nSolution: {solution.maxSubArray(testcases[i])}\n")


