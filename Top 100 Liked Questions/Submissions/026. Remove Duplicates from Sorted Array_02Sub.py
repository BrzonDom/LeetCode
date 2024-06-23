"""
26. Remove Duplicates from Sorted Array

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

    Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

        Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
        Return k.


    Custom Judge:

        The judge will test your solution with the following code:

        int[] nums = [...]; // Input array
        int[] expectedNums = [...]; // The expected answer with correct length

        int k = removeDuplicates(nums); // Calls your implementation

        assert k == expectedNums.length;
        for (int i = 0; i < k; i++) {
            assert nums[i] == expectedNums[i];
        }
        If all assertions pass, then your solution will be accepted


    Example 1:

        Input: nums = [1, 1, 2]
        Output: 2, nums = [1, 2, _]

        Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
            It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:

        Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]

        Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
            It does not matter what you leave beyond the returned k (hence they are underscores).


    Constraints:

        1 <= nums.length <= 3 * 10^4
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.

"""


def Sol01A_ItrSet_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case\n")

        inLst = case

        print(f"\tInput List: {inLst}")
        print()

        numSet = set()
        dupCnt = 0
        numCnt = 0

        for num in inLst:

            if num in numSet:

                dupCnt += 1
            else:
                numSet.add(num)
                numCnt += 1

        print(f"\t\tList Set: {numSet}")
        print()

        setLst = list(numSet)
        dupLst = ["_" for dup in range(dupCnt)]

        print(f"\t\tSet List:  {setLst}")
        print(f"\t\tDup. List: {dupLst}")
        print()

        outLst = list(map(str, setLst)) + dupLst

        print(f"\tOut List: ", end="[")
        for i, itm in enumerate(outLst):
            if (i + 1) >= len(outLst):

                print(f"{itm}]")
            else:
                print(f"{itm}, ", end="")
        print()

        print(f"\t\tNumbers:    {numCnt}")
        print(f"\t\tDuplicates: {dupCnt}")

        print("\n")


def Sol01_ItrSet_Prt(inLst):

    print(f"\tInput List: {inLst}")
    print()

    numSet = set()
    dupCnt = 0
    numCnt = 0

    for num in inLst:

        if num in numSet:

            dupCnt += 1
        else:
            numSet.add(num)
            numCnt += 1

    print(f"\t\tList Set: {numSet}")
    print()

    setLst = list(numSet)
    dupLst = ["_" for dup in range(dupCnt)]

    print(f"\t\tSet List:  {setLst}")
    print(f"\t\tDup. List: {dupLst}")
    print()

    outLst = list(map(str, setLst)) + dupLst

    print(f"\tOut List: ", end="[")
    for i, itm in enumerate(outLst):
        if (i + 1) >= len(outLst):

            print(f"{itm}]")
        else:
            print(f"{itm}, ", end="")
    print()

    print(f"\t\tNumbers:    {numCnt}")
    print(f"\t\tDuplicates: {dupCnt}")

    print("\n")


def Sol02A_WhlPop_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case\n")

        inLst = case
        orgLen = len(inLst)

        print(f"\tInput List: {inLst}")
        print(f"\t\tOrg. len.: {orgLen}")
        print()

        i = 1
        while i < len(inLst):

            if inLst[i] == inLst[i - 1]:
                inLst.pop(i)

            else:
                i += 1

        outLen = len(inLst)
        dupLen = orgLen - outLen

        print(f"\tOutput List: {inLst}")
        print(f"\t\tOut  len.: {outLen}")
        print(f"\t\tDup. len.: {dupLen}")

        print("\n")


def Sol02_WhlPop_Prt(inLst):

    orgLen = len(inLst)

    print(f"\tInput List: {inLst}")
    print(f"\t\tOrg. len.: {orgLen}")
    print()

    i = 1
    while i < len(inLst):

        if inLst[i] == inLst[i - 1]:
            inLst.pop(i)

        else:
            i += 1

    outLen = len(inLst)
    dupLen = orgLen - outLen

    print(f"\tOutput List: {inLst}")
    print(f"\t\tOut  len.: {outLen}")
    print(f"\t\tDup. len.: {dupLen}")

    print("\n")

    return outLen


def Sol03A_SlwFstPnt_Prt(InLst):

    for csCnt, case in enumerate(InLst):

        print(f"{csCnt + 1}. Case\n")

        inLst = case
        orgLen = len(inLst)

        print(f"\tInput List: {inLst}")
        print(f"\t\tOrg. len.: {orgLen}")
        print()

        dupCnt = 0

        slwP = 0
        fstP = 1

        while fstP < len(inLst):

            if inLst[slwP] == inLst[fstP]:
                fstP += 1

                dupCnt += 1

            else:
                inLst[slwP + 1] = inLst[fstP]

                fstP += 1
                slwP += 1

        outLen = slwP + 1
        dupLen = orgLen - outLen

        print(f"\tOut List: {inLst[:outLen]}")
        print(f"\t\tOut  len.: {outLen}")
        print(f"\t\tDup. len.: {dupLen}")
        # print(f"\t\tDup. cnt.: {dupCnt}")

        print("\n")


def Sol03_SlwFstPnt_Prt(inLst):

    orgLen = len(inLst)

    print(f"\tInput List: {inLst}")
    print(f"\t\tOrg. len.: {orgLen}")
    print()

    dupCnt = 0

    slwP = 0
    fstP = 1

    while fstP < len(inLst):

        if inLst[slwP] == inLst[fstP]:
            fstP += 1

            dupCnt += 1

        else:
            inLst[slwP + 1] = inLst[fstP]

            fstP += 1
            slwP += 1

    outLen = slwP + 1
    dupLen = orgLen - outLen

    print(f"\tOut List: {inLst[:outLen]}")
    print(f"\t\tOut  len.: {outLen}")
    print(f"\t\tDup. len.: {dupLen}")
    # print(f"\t\tDup. cnt.: {dupCnt}")

    print("\n")

    return outLen


if __name__ == '__main__':

    InputLst = [[1, 1, 2],
                [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]

    # Sol01A_ItrSet_Prt(InputLst)

    # Sol02A_WhlPop_Prt(InputLst)

    # Sol03A_SlwFstPnt_Prt(InputLst)

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}. Case\n")

        # Sol01_ItrSet_Prt(case)

        # Sol02_WhlPop_Prt(case)

        Sol03_SlwFstPnt_Prt(case)

