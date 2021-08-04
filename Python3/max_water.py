from typing import List

# Given n non-negative integers a1, a2, ..., an , where each represents 
# a point at coordinate (i, ai). n vertical lines are drawn such that 
# the two endpoints of the line i is at (i, ai) and (i, 0). Find two 
# lines, which, together with the x-axis forms a container, such that 
# the container contains the most water.
#
# You may not slant the container.
#
# Constraints:
#   - n == height.length
#   - 2 <= n <= 105
#   - 0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max = 0

        while l < r:

            if height[l] > height[r]:
                test = height[r] * (r - l)
                r -= 1
                if test > max:
                    max = test
                
            else:
                test = height[l] * (r - l)
                l += 1
                if test > max:
                    max = test

        return max