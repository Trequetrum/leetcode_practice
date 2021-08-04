from typing import List

# Given an array of integers nums containing n + 1 integers 
# where each integer is in the range [1, n] inclusive.
#
# There is only one repeated number in nums, return this 
# repeated number.
#
# You must solve the problem without modifying the array 
# nums and uses only constant extra space.
#
# Constraints:
#   - 1 <= n <= 105
#   - nums.length == n + 1
#   - 1 <= nums[i] <= n
#   - All the integers in nums appear only once except for 
#       precisely one integer which appears two or more times.
#
# Follow-ups:
#   - How can we prove that at least one duplicate number 
#       must exist in nums?
#   - Can you solve the problem in linear runtime complexity?

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hits = {}
        for n in nums:
            if n in hits:
                return n
            # Not constant space, doesn't solve this problem as-is
            else: hits[n] = 1 