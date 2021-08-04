from typing import List

# Given an unsorted integer array nums, return the smallest missing 
# positive integer. You must implement an algorithm that runs in O(n) 
# time and uses constant extra space.
#
# Constraints:
#   - 1 <= nums.length <= 5 * 105
#   - -231 <= nums[i] <= 231 - 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        pool = set(nums)
        max = len(nums) + 1
        for n in range(1, max):
            if n not in pool:
                return n
        return max


get = Solution()
#print(get.firstMissingPositive([3,4,-1,1]))
print(get.firstMissingPositive([1]))