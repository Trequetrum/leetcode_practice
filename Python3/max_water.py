from typing import List

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