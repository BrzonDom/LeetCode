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
import copy

def findTargSum_Sol(numArr, targ):

    for nRang in range(len(numArr)):
        numSum = 0
        indTarg = []

        for n, num in enumerate(numArr[nRang:]):

            indTarg.append(n + nRang)
            numSum += num

            if numSum == targ:

                return indTarg


def findTargSum_Stp(numArr, targ):

    print("\tNumbers array:", numArr)
    print("\t       Target:", targ)
    print()

    for nRang in range(len(numArr)):
        numComb = ""
        numSum = 0
        numInd = []

        for n, num in enumerate(numArr[nRang:]):
            # print(num, end=", ")
            numInd.append(n + nRang)
            numComb += f"{num} + "
            numSum += num
            print(f"\t\t{numSum:2} = {numComb[:-3]}")

            if numSum == targ:
                sumTarg = f"{numSum:2} = {numComb[:-3]}"
                indTarg = copy.deepcopy(numInd)

                print("\n\t\tTarget sum:", sumTarg)
                print("\t\t\tTarget index:", indTarg)
                # print("\n")

                return indTarg


def findTargSum_Prt(numArr, targ):

    print("\tNumbers array:", numArr)
    print("\t       Target:", targ)
    print()

    for nRang in range(len(numArr)):
        numComb = ""
        numSum = 0
        numInd = []

        for n, num in enumerate(numArr[nRang:]):
            # print(num, end=", ")
            numInd.append(n + nRang)
            numComb += f"{num} + "
            numSum += num
            print(f"\t\t{numSum:2} = {numComb[:-3]}")

            if numSum == targ:
                sumTarg = f"{numSum:2} = {numComb[:-3]}"
                indTarg = copy.deepcopy(numInd)

    print("\n\t\tTarget sum:", sumTarg)
    print("\t\t\tTarget index:", indTarg)
    print("\n")

    return indTarg



Input_numsLst = [[[2, 7, 11, 15], 9],
                 [[3, 2, 4], 6],
                 [[3, 3], 6]]

print("Driver solution:\n")

for numLst in Input_numsLst:
    numArr = numLst[0]
    targ = numLst[1]

    print("\tNumbers array:", numArr)
    print("\t       Target:", targ)
    print()

    for nRang in range(len(numArr)):
        numComb = ""
        numSum = 0
        numInd = []

        for n, num in enumerate(numArr[nRang:]):
            # print(num, end=", ")
            numInd.append(n + nRang)
            numComb += f"{num} + "
            numSum += num
            print(f"\t\t{numSum:2} = {numComb[:-3]}")

            if numSum == targ:
                sumTarg = f"{numSum:2} = {numComb[:-3]}"
                indTarg = copy.deepcopy(numInd)

    print("\n\t\tTarget sum:", sumTarg)
    print("\t\t\tTarget index:", indTarg)
    print("\n")


print("Function print solution:\n")

for numLst in Input_numsLst:
    numArr = numLst[0]
    targ = numLst[1]

    findTargSum_Prt(numArr, targ)

print("Function stop and solve solution:\n")

for numLst in Input_numsLst:
    numArr = numLst[0]
    targ = numLst[1]

    findTargSum_Stp(numArr, targ)
    print(f"\t\t\tTarget index: {findTargSum_Sol(numArr, targ)}")
    print("\n")
