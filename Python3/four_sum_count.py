from typing import List

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