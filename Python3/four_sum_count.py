from typing import List

# Given four integer arrays nums1, nums2, nums3, and nums4 all of 
# length n, return the number of tuples (i, j, k, l) such that:
#   - 0 <= i, j, k, l < n
#   - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
# Constraints:
#   - n == nums1.length
#   - n == nums2.length
#   - n == nums3.length
#   - n == nums4.length
#   - 1 <= n <= 200
#   - -228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        acc12 = {}
        for v1 in nums1:
            for v2 in nums2:
                sum = v1 + v2
                if sum in acc12:
                    acc12[sum] += 1
                else:
                    acc12[sum] = 1

        res = 0
        for v1 in nums3:
            for v2 in nums4:
                sum = v1 + v2
                if -sum in acc12:
                    res += acc12[-sum]  
        
        return res