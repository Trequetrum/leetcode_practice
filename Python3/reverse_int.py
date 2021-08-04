
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


