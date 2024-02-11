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

def findMedianV2_Prt(arrLst):

    arr1 = arrLst[0]
    arr2 = arrLst[1]

    print("\t1. Array: ", arr1)
    print("\t2. Array: ", arr2)
    print()

    arr = sorted(arr1 + arr2)
    print("\tArray: ", arr)
    print()

    lenAr = len(arr)
    medInd = lenAr // 2


    print("\t\tMedian index: ", medInd)
    print()

    if lenAr % 2:

        median = float(arr[medInd])

        print("\t\tMedian: ", median)
        print()

        return median

    else:

        med1 = float(arr[medInd-1])
        med2 = float(arr[medInd])
        median = (med1 + med2) / 2

        print("\t\tMedian: ", median)
        print()

        return median


def fndMedianV1_Prt(arrLst):

    arr1 = arrLst[0]
    arr2 = arrLst[1]

    print("\t1. Array: ", arr1)
    print("\t2. Array: ", arr2)
    print()

    lenAr1 = len(arr1)
    lenAr2 = len(arr2)

    medIndAr1 = lenAr1 // 2
    medIndAr2 = lenAr2 // 2


    print("\t\t1. Median index: ", medIndAr1)
    print("\t\t2. Median index: ", medIndAr2)
    print()


    if lenAr1 == 1:

        medAr1 = float(arr1[0])

    elif lenAr1 % 2 == 0:

        medAr1 = arr1[medIndAr1-1] + arr1[medIndAr1]
        medAr1 /= 2

    else:
        medAr1 = float(arr1[medIndAr1])



    if lenAr2 == 1:

        medAr2 = float(arr2[0])

    elif lenAr2 % 2 == 0:

        medAr2 = arr2[medIndAr2-1] + arr2[medIndAr2]
        medAr2 /= 2

    else:
        medAr2 = float(arr2[medIndAr2])

    median = (medAr1 + medAr2) / 2

    print("\t\t1. Median: ", medAr1)
    print("\t\t2. Median: ", medAr2)
    print("")
    print("\t\tMedian: ", median)
    # print("\n")

    return median


Input_ArrLst = [[[1, 3], [2]],
                [[1, 2], [3, 4]],
                [[1, 2, 3, 5, 6], [2, 4, 4, 6]]]

print("Driver solution:\n")

for arrLst in Input_ArrLst:

    print("\t1. Array: ", arrLst[0])
    print("\t2. Array: ", arrLst[1])
    print("")

    arr1 = arrLst[0]
    arr2 = arrLst[1]

    lenAr1 = len(arr1)
    lenAr2 = len(arr2)

    medIndAr1 = lenAr1 // 2
    medIndAr2 = lenAr2 // 2


    print("\t\t1. Median index: ", medIndAr1)
    print("\t\t2. Median index: ", medIndAr2)
    print()
    # print(1 % 2 == 0)

    if lenAr1 == 1:

        medAr1 = float(arr1[0])

    elif lenAr1 % 2 == 0:

        medAr1 = arr1[medIndAr1-1] + arr1[medIndAr1]
        medAr1 /= 2

    else:
        medAr1 = float(arr1[medIndAr1])


    if lenAr2 == 0:

        medAr2 = float(arr2[0])

    elif lenAr2 % 2 == 0:

        medAr2 = arr2[medIndAr2-1] + arr2[medIndAr2]
        medAr2 /= 2

    else:
        medAr2 = float(arr2[medIndAr2])

    print("\t\t1. Median: ", medAr1)
    print("\t\t2. Median: ", medAr2)
    print("")

    median = (medAr1 + medAr2) / 2

    print("\t\tMedian: ", median)
    print("\n")

print()

print("1. Function solution:\n")

for arrLst in Input_ArrLst:

    median = fndMedianV1_Prt(arrLst)
    print("\t\tMedian: ", median)
    print("\n")

print("2. Function solution:\n")

for arrLst in Input_ArrLst:

    findMedianV2_Prt(arrLst)
    print()
