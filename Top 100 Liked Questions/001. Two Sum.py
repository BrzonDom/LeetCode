"""
1. Two Sum

https://leetcode.com/problems/two-sum/description/

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]

    Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]

"""

Input_numsLst = [[[2, 7, 11, 15], 9],
                 [[3, 2, 4], 6],
                 [[3, 3], 6]]

for numLst in Input_numsLst:
    numArr = numLst[0]
    targ = numLst[1]

    print("\tNumbers array:", numArr)
    print("\t       Target:", targ)
    print()

    for nRang in range(len(numArr)):
        numComb = ""
        numSum = 0
        for num in numArr[nRang:]:
            # print(num, end=", ")
            numComb += f"{num} + "
            numSum += num
            print(f"\t\t{numSum:2} = {numComb[:-3]}")
        # numComb = numComb[:-2] + f"= {numSum}"
        # print("\t\t", numComb)
    print()
