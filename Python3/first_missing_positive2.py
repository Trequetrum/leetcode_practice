from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        length = len(nums)
        lookup = [-1 for x in range(length)]
        
        max = length + 1
        for v in nums:
            if v > 0 and v < max:
                lookup[v-1] = v

        #print(f"sorted: {nums}")
        for i in range(length):
            if lookup[i] == -1:
                return i + 1
        
        return max


nums = [0,0,0,0,0,0,0]
lookup = [-1 for x in range(len(nums))]
print(lookup)
get = Solution()
print(get.firstMissingPositive([3,4,-1,1]))