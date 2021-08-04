# Given a signed 32-bit integer x, return x with its digits 
# reversed. If reversing x causes the value to go outside 
# the signed 32-bit integer range [-231, 231 - 1], then 
# return 0.
#
# Assume the environment does not allow you to store 64-bit 
# integers (signed or unsigned).
#
# Constraints:
#   - -231 <= x <= 231 - 1

class Solution:
    def reverse(self, x: int) -> int:
        parse = int(str(abs(x))[::-1])
        if x > 0 and parse < 2**31 - 1:
            return parse
        elif x < 0 and (-1) * parse > -2**31:
            return (-1) * parse
          
        return 0

get = Solution()
print(get.reverse(123))
print(get.reverse(-123))


