from typing import List

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