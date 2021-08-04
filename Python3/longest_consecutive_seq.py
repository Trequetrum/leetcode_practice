from typing import List

# Given an unsorted array of integers nums, return the length of the 
# longest consecutive elements sequence. You must write an algorithm 
# that runs in O(n) time.
#
# Constraints:
#   - 0 <= nums.length <= 105
#   - -109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        longest = 0

        for e in pool:
            if e - 1 not in pool:
                check = e + 1
                while check in pool:
                    check += 1
                longest = max(longest, check - e)
                
        return longest