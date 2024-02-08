"""
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

    Input:
        nums = [1,2,3,4]

    Output:
        [1,3,6,10]

    Explanation:
        Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

    Input:
        nums = [1,1,1,1,1]

    Output:
        [1,2,3,4,5]

    Explanation:
        Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

    Input:
        nums = [3,1,2,10,1]
    Output:
        [3,4,6,16,17]


Constraints:

    1 <= nums.length <= 1000
    -10^6 <= nums[i] <= 10^6

"""


class sumSol():
    def run(self, numLst):
        sumLst = [numLst[0]]

        for num in numLst[1:]:
            sumLst.append(sumLst[-1] + num)

        return sumLst


def runSumV1(numLst):

    sumLst = []
    sum = 0
    for num in numLst:
        sum += num
        sumLst.append(sum)

    return sumLst

def runSumV2(numLst):

    sumLst = [numLst[0]]

    for num in numLst[1:]:
        sumLst.append(sumLst[-1] + num)

    return sumLst

Input_NumLst = [[1, 2, 3, 4],
             [1, 1, 1, 1, 1],
             [3, 1, 2, 10, 1]]

Out_Lst = []

print("Driver solution:\n")

for NumLst in Input_NumLst:
    sum = 0
    print(f"\tInput:  {NumLst}")
    for num in NumLst:
        sum += num
        Out_Lst.append(sum)

    print(f"\tOutput: {Out_Lst}\n\n")
    # print(Out_Lst)
    Out_Lst = []


print("1.Function solution:\n")

for numLst in Input_NumLst:
    print(f"\tInput:  {NumLst}")

    Out_Lst = runSumV1(numLst)
    print(f"\tOutput: {Out_Lst}\n\n")


print("2.Function solution:\n")

for numLst in Input_NumLst:
    print(f"\tInput:  {NumLst}")

    Out_Lst = runSumV2(numLst)
    print(f"\tOutput: {Out_Lst}\n\n")


print("Class solution:\n")

for numLst in Input_NumLst:
    print(f"\tInput:  {NumLst}")

    Cls_Lst = sumSol()
    Out_Lst = Cls_Lst.run(numLst)
    print(f"\tOutput: {Out_Lst}\n\n")
