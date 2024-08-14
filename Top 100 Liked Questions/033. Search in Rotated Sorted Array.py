"""
33. Search in Rotated Sorted Array

https://leetcode.com/problems/search-in-rotated-sorted-array/description/


    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
    such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0, 1, 2, 4, 5, 6, 7] might be rotated at pivot index 3 and become [4, 5, 6, 7, 0, 1, 2].

    Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
    or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.


    Example 1:

        Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
        Output: 4

    Example 2:

        Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
        Output: -1

    Example 3:

        Input: nums = [1], target = 0
        Output: -1


    Constraints:

        1 <= nums.length <= 5000
        -10^4 <= nums[i] <= 10^4
        All values of nums are unique.
        nums is an ascending array that is possibly rotated.
        -10^4 <= target <= 10^4

"""


InputLst = [[[4, 5, 6, 7, 0, 1, 2], 0],
            [[4, 5, 6, 7, 0, 1, 2], 3],
            [[1], 0]]

for csCnt, case in enumerate(InputLst):

    print(f"{csCnt+1}.Case\n")

    Arr = case[0]
    Trg = case[1]

    print(f"\tArray: {Arr}")
    print(f"\tTarget: {Trg}")
    print()

    ln = len(Arr)
    print(f"\tLength: {ln}")
    print()

    iSt = 0
    iEn = ln - 1
    iMd = (iSt + iEn) // 2

    nSt = Arr[iSt]
    nEn = Arr[iEn]
    nMd = Arr[iMd]

    print(f"\t\t1. Start: {nSt} = Arr[{iSt}]")
    print(f"\t\t1. End:   {nEn} = Arr[{iEn}]")
    print(f"\t\t1. Mid:   {nMd} = Arr[{iMd}]")
    print()

    stpCnt = 1

    while iSt < iEn:
        stpCnt += 1

        if nMd < Trg:

            iSt = iMd + 1
            iMd = (iSt + iEn) // 2

            nSt = Arr[iSt]
            nMd = Arr[iMd]

            print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{iSt}]")
            print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{iEn}]")
            print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{iMd}]")
            print()

        elif nMd > Trg and nSt <= Trg:

            iSt = iSt + 1
            iEn = iMd - 1
            iMd = (iSt + iEn) // 2

            nSt = Arr[iSt]
            nEn = Arr[iEn]
            nMd = Arr[iMd]

            print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{iSt}]")
            print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{iEn}]")
            print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{iMd}]")
            print()

        elif nMd > Trg and nSt > Trg:

            iSt = iMd + 1
            iMd = (iSt + iEn) // 2

            nSt = Arr[iSt]
            nEn = Arr[iEn]
            nMd = Arr[iMd]

            print(f"\t\t{stpCnt}. Start: {nSt} = Arr[{iSt}]")
            print(f"\t\t{stpCnt}. End:   {nEn} = Arr[{iEn}]")
            print(f"\t\t{stpCnt}. Mid:   {nMd} = Arr[{iMd}]")
            print()

        if nMd == Trg:

            print(f"\tTarget found on index: {iMd}")
            print()

            break

    print("\n")
