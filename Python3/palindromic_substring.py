
# Expand out from the lower and upper pointers until we're no longer a
# palindrome, then return the biggest palindrom we could find from the
# given bounds
def biggestFrom(string, lower, upper):
    try:
        while lower - 1 > -1 and string[lower - 1] == string[upper + 1]:
            lower = lower - 1
            upper = upper + 1
    except IndexError: 
        pass

    return string[lower: upper + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:

        sLen = len(s)

        if sLen < 2:
            return s
        
        # We can find the middle of a palindrome if we have 3 
        # characters to look at. aa and aba, once we find the middle
        # we can search outward to check how large the palindrom is.
        #
        # First, we need at least 3 characters, so deal with the cases
        # where that isn't the case.
        longest = s[0]
        if s[0] == s[1]: longest = s[0:2]
        if sLen == 2: return longest

        # The size of our window into the string never changes, so one
        # pointer is all we need to keep track of whre this window is.
        end = 2

        # Find the middle of every palindrom in the input string
        while end < sLen:

            start = end - 2
            mid = end - 1

            if s[mid] == s[end]:
                found = biggestFrom(s, mid, end)
                if len(found) > len(longest): longest = found
            if s[start] == s[end]:
                found = biggestFrom(s, start, end)
                if len(found) > len(longest): longest = found

            end += 1

        return longest

get = Solution()
tests = [   ""
        ,   "a"
        ,   "ac"
        ,   "abba"
        ,   "babad"
        ,   "eabcbad"
        ,   "abcyy"
        ,   "abcyzy"
        ,   "ada"
        ,   "adam"
        ]

for test in tests:
    pass
    v = get.longestPalindrome(test)
    print(v)
