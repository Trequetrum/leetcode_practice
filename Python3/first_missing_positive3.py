from typing import List

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