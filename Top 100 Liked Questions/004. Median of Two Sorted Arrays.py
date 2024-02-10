"""
4. Median of Two Sorted Arrays

https://leetcode.com/problems/median-of-two-sorted-arrays/

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).



    Example 1:

        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.

    Example 2:

        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    Constraints:

        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -10⁶ <= nums1[i], nums2[i] <= 10⁶
"""

Input_ArrLst = [[[1, 3], [2]],
                [[1, 2], [3, 4]]]

print("Driver solution:\n")

for arrLst in Input_ArrLst:

    print("\t1. Array: ", arrLst[0])
    print("\t2. Array: ", arrLst[1])
    print("\n")

    arr1 = arrLst[0]
    arr2 = arrLst[1]
