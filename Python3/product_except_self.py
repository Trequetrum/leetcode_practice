# Given an integer array nums, return an array answer such that 
# answer[i] is equal to the product of all the elements of nums 
# except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to 
# fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without 
# using the division operation.
#
# Constraints:
#   - 2 <= nums.length <= 105
#   - -30 <= nums[i] <= 30
#   - The product of any prefix or suffix of nums is guaranteed 
#       to fit in a 32-bit integer.
#
# Follow up: Can you solve the problem in O(1) extra space complexity? 
# (The output array does not count as extra space for space complexity 
# analysis.)

class Solution:
    def productExceptSelf(self, nums):

        length = len(nums)

        if length < 1: return []
        if length == 1: return [0]

        res = [nums[0]]

        for i in range(1, length - 1):
            res.append(res[i - 1] * nums[i])
        res.append(res[length - 2])

        right = 1

        for i in range(length - 1, 0, -1):
            res[i] = res[i - 1] * right
            right = right * nums[i]
        res[0] = right

        return res
        


get = Solution()
print(get.productExceptSelf([-1,1,0,-3,3]))