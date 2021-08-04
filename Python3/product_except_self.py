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