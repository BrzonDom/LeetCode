"""
2022. Convert 1D Array Into 2D Array

https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=daily-question&envId=2024-09-01

        Day: 2024/09/01

    You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with
     creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.

    The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
    the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array,
    and so on.

    Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.


    Example 1:

        Input: original = [1, 2, 3, 4], m = 2, n = 2

        Output: [[1, 2], [3, 4]]

        Explanation: The constructed 2D array should contain 2 rows and 2 columns.
            The first group of n=2 elements in original, [1, 2], becomes the first row in the constructed 2D array.
            The second group of n=2 elements in original, [3, 4], becomes the second row in the constructed 2D array.

    Example 2:

        Input: original = [1, 2, 3], m = 1, n = 3

        Output: [[1, 2, 3]]

        Explanation: The constructed 2D array should contain 1 row and 3 columns.
            Put all three elements in original into the first row of the constructed 2D array.

    Example 3:

        Input: original = [1, 2], m = 1, n = 1

        Output: []

        Explanation: There are 2 elements in original.
            It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.


    Constraints:

        1 <= original.length <= 5 * 10^4
        1 <= original[i] <= 10^5
        1 <= m, n <= 4 * 10^4

"""


def Slt01_MtrxCntIdx_Prt(Arry, DmRw, DmCl):

    lnAr = len(Arry)

    print(f"\tArray: {Arry}")
    print(f"\t\tLength: {lnAr}")
    print()

    print("\tDimensions:")
    print(f"\t\tRows: {DmRw}")
    print(f"\t\tCols: {DmCl}")
    print()

    if lnAr != DmRw * DmCl:
        print("\tArray doesn't fit into the matrix")

        return []

    mtrx = [[0 for c in range(DmCl)] for r in range(DmRw)]

    idxCnt = 0
    for r, row in enumerate(mtrx):
        for c, col in enumerate(row):
            mtrx[r][c] = Arry[idxCnt]

            idxCnt += 1

    print("\tMatrix:")
    for row in mtrx:
        print(f"\t\t{row}")

    return mtrx


def Slt02_MtrxAppRw_Prt(Arry, DmRw, DmCl):

    lnAr = len(Arry)

    print(f"\tArray: {Arry}")
    print(f"\t\tLength: {lnAr}")
    print()
    print(f"\t\tRows: {DmRw}")
    print(f"\t\tCols: {DmCl}")
    print()

    if lnAr != DmCl * DmRw:

        return []

    mtrx = []

    print("\tMatrix:")
    for idx in range(0, lnAr, DmCl):
        print(f"\t\t{Arry[idx: idx + DmCl]}")

        mtrx.append(Arry[idx: idx + DmCl])

    return


if __name__ == "__main__":

    InputLst = [[[1, 2, 3, 4], 2, 2],
                [[1, 2, 3], 1, 3],
                [[1, 2], 1, 1]]

    for csCnt, case in enumerate(InputLst):

        print(f"{csCnt + 1}.Case\n")

        # Slt01_MtrxCntIdx_Prt(case[0], case[1], case[2])

        Arry = case[0]
        lnAr = len(Arry)

        DmRw = case[1]
        DmCl = case[2]

        print(f"\tArray: {Arry}")
        print(f"\t\tLength: {lnAr}")
        print()

        print(f"\t\tRows: {DmRw}")
        print(f"\t\tCols: {DmCl}")
        print()

        if lnAr != DmCl * DmRw:
            print("\tArray doesn't fit into the matrix")

            print("\n")
            continue

        mtrx = []

        print("\tMatrix:")
        for idx in range(0, lnAr, DmCl):
            print(f"\t\t{Arry[idx: idx + DmCl]}")

            mtrx.append(Arry[idx: idx + DmCl])

        print("\n")
