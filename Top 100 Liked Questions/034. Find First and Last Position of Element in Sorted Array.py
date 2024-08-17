"""
34. Find First and Last Position of Element in Sorted Array

https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of
    a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.


    Example 1:

        Input: nums = [5, 7, 7, 8, 8, 10], target = 8
        Output: [3, 4]

    Example 2:

        Input: nums = [5, 7, 7, 8, 8, 10], target = 6
        Output: [-1, -1]

    Example 3:

        Input: nums = [], target = 0
        Output: [-1, -1]


    Constraints:

        0 <= nums.length <= 10^5
        -10^9 <= nums[i] <= 10^9
        nums is a non-decreasing array.
        -10^9 <= target <= 10^9

"""


InputLst = [[[5, 7, 7, 8, 8, 10], 8],
            [[5, 7, 7, 8, 8, 10], 6],
            [[], 0]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt+1}.Case\n")

    Arr = case[0]
    Trg = case[1]

    print(f"\tArray: {Arr}")
    print(f"\tTarget: {Trg}")
    print()

    ln = len(Arr)
    print(f"\t\tLength: {ln}")
    print()

    St = 0
    En = ln - 1
    Md = (St + En) // 2

    nSt = Arr[St]
    nEn = Arr[En]
    nMd = Arr[Md]

    print(f"\t\tStart: {nSt}")
    print(f"\t\tEnd:   {nEn}")
    print(f"\t\tMid:   {nMd}")

    print("\n")