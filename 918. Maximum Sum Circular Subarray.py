# Solution code for 
# 918. Maximum Sum Circular Subarray

from typing import List
import random
import pyperclip

class Solution:
    def maxSubarraySumCircular(self, nums : List[int]) -> int:
        n = len(nums)
        max_so_far, min_so_far = nums[0], nums[0]
        min_ending_here, max_ending_here = nums[0], nums[0]
        total = nums[0]

        for i in range(1, n):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            min_ending_here = min(min_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
            min_so_far = min(min_so_far, min_ending_here)
            total += nums[i]
        
        if total == min_so_far:
            print("Solution:", max_so_far, "\n")
            return max_so_far
        
        print("Solution:", max(max_so_far, total - min_so_far), "\n")
        return max(max_so_far, total - min_so_far)
        
testcases = [
    [1,-2,3,-2],  # ans = 3
    [5,-3,5],  # ans = 10
    [-3,-2,-3],  # ans = -2
    [-17, 19, 9, 20, 6, -2, -3, 20, 12, 10, -19, -26, 8, 1, -10, -4, 22, -6, 1, -13, 23, 4, -14, 5, -20, 14, 30, 26, -8],  # ans = 138
    [-2, 10, 5, -15, 1, 10],  # ans = 24
    [-1, -6, -29, -9, 26, -19, 11, -4, 4, -10, 4, 15, 8, 20, -23, -7, -15, -6, 1, -23, -15, 28, 2, -12, 26, 28, -18, 7, 18],  # ans = 89
    [random.randint(-100, 100) for i in range(random.randint(1, 100))]
]

solution = Solution()

print ()
for i, case in enumerate(testcases):
    print (f"\nCase #{i+1}:\n{case}")
    solution.maxSubarraySumCircular(case)