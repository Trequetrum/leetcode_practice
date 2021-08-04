from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # The largest first missing positive that could 
        # exist given the input array
        max = len(nums) + 1

        # Iterate through the array, swap any values we're interested
        # in in their corresponding spot in the array. Numbers we're not
        # interested in are set to -1.
        i = 0
        while i < len(nums):
            v = nums[i]
            if v > 0 and v < max:
                
                # Account for duplicates or numbers that are already in place
                if nums[v - 1] == v:
                    if i != v - 1:
                        nums[i] = -1
                else:
                    # print(f"found v:{v}, assigning i:{v -1}, swapping:{nums[v - 1]}")
                    # Perform the swap
                    tmp = nums[v - 1]
                    nums[v - 1] = v
                    if tmp > 0 and tmp < max:
                        nums[i] = tmp
                        i -= 1 # Don't incrememnt if we've swapped a interesting number
                    else: nums[i] = -1

            else: nums[i] = -1

            i += 1

        # print(f"kinda-sorted: {nums}")
        for i, v in enumerate(nums):
            if v == -1:
                return i + 1
        
        return max


    

get = Solution()
print(get.firstMissingPositive([3,4,8,1]))