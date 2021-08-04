from math import floor, ceil

def findMedianInSortedNums(nums1, nums2):

    # Some constant values
    len1 = len(nums1)
    len2 = len(nums2)
    len_comb = len1 + len2

    # Two empty arrays is against spec
    if len_comb < 1:
        raise ValueError("Cannot find median from two empty arrays")

    # We want to figure out how many elements of each array are below
    # the median number. This means there's no easy way to tell the
    # difference between an empty array and an array for which no
    # elements are below the median.
    #
    # To deal with this, we treat the cases where either array is empty
    # or both arrays have just 1 element as special cases. This way we 
    # don't need to insert any checks to account for them later.
    simple = None
    if len1 < 1:
        simple = nums2
    if len2 < 1:
        simple = nums1

    if simple != None:
        # Return the median of the sorted array `simple`
        lenS = len(simple)
        mid = floor(lenS / 2)
        if lenS % 2 == 0:
            return (simple[mid] + simple[mid - 1]) / 2
        else:
            return simple[mid]
    

    if len_comb == 2:
        # The median is the average of our two numbers
        return (nums1[0] + nums2[0]) / 2

    # If we make it this far, we know there are at least 3 elements
    # and they're split between two arrays. We're ready to figure 
    # out which elements are in the left parition 

    # Parition_length includes the median. 
    # len_comb >= 3 implies parition_length >= 2
    parition_length = ceil(len_comb / 2) 
    partition_even = len_comb % 2 == 0

    # Nieve guess at pointers a left parition for each array
    left1 = max(floor(len1 / 2) - 1, 0)
    left2 = parition_length - left1 - 2

    # Adjust pointers to get the actual left parition
    while left1 > -1 and left2 > -1:

        if gt_def_false(nums1[left1], safe_index(nums2, left2 + 1)):
            left1 -= 1
            left2 += 1
        elif gt_def_false(nums2[left2], safe_index(nums1, left1 + 1)):
            left1 += 1
            left2 -= 1
        else: break

    # We have the left parition
    #
    # What follows is verbose. If we:
    #   - create a max function that accepts 'None' and has 
    #       reasonable outputs 
    #   - alter safe_index to return 'None' for negative indices 
    #       (-1 specifically) 
    # Then else-clause below covers all three cases.
    #
    # We don't do that here because this runs faster on leetcode when
    # unrolled like this. Also, inlining these function calls is fast
    # (though still slower) but turns this into an unreadable mess.

    # All the elements below the median are in the right array
    if left1 <= -1:
        if partition_even:
            high = none_min(safe_index(nums2, left2 + 1), nums1[0])
            return (nums2[left2] + high) / 2
        else: 
            return nums2[left2]
    # All the elements below the median are in the left array
    elif left2 <= -1:
        if partition_even:
            high = none_min(safe_index(nums1, left1 + 1), nums2[0])
            return (nums1[left1] + high) / 2
        else: 
            return nums1[left1]
    # The common case, both arrays have some elements below the median
    else:
        if partition_even:
            return (
                    max(nums1[left1], nums2[left2]) + 
                    none_min(
                        safe_index(nums1, left1 + 1), 
                        safe_index(nums2, left2 + 1)
                    )
                ) / 2
        else: 
            return max(nums1[left1], nums2[left2])


# Greater than logical operator that accepts 'None',
# Returns false if either input is 'None'
def gt_def_false(a, b):
    if a == None or b == None:
        return False
    else: return a > b

# Min function that accepts 'None', returns 'None' if
# both inputs are 'None'
def none_min(a,b):
    if a == None:
        return b
    elif b == None:
        return a
    else: return min(a, b)

# If indexing fails, return 'None' instead of crashing
def safe_index(array, index):
    try: return array[index]
    except IndexError: return None

# Tests, don't mind the strange formatting
tests = [   [[0],                   [0]]
        ,   [[0,0],                 [0,0]]
        ,   [[1],                   [2,3,4]]
        ,   [[4],                   [1,2,3]]
        ,   [[],                    [0]]
        ,   [[0],                   []]
        ,   [[1],                   [2]]
        ,   [[1,3,5,7],             [2,4,5,8,10,12,14,16]]
        ,   [[2,4,5,8,10,12,14,16], [1,3,5,7]]
        ,   [[1,2,3,8],             [2,3,4,8]]
        ,   [[3],                   [3,4]]
        ,   [[1,2,3],               [4,5,6]]
        ,   [[1,2,4],               [3,5,6]]
        ,   [[-2,-1],               [-3,5]]
        ]

# Run our tests
for test in tests:
    print(f"left: {test[0]}, right: {test[1]}")
    v = findMedianInSortedNums(test[0], test[1])
    print(f"X: {v}")
